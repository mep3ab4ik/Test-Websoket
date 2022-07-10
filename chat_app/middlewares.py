import logging

import jwt
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings

from account_app.models import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@database_sync_to_async
def get_user(query_string):
    encoded_token = query_string.removeprefix('token=')
    try:
        token = jwt.decode(encoded_token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.DecodeError:
        return None

    try:
        return User.objects.get(id=token['id'])
    except User.DoesNotExist:
        return None


class QueryAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        scope['user'] = await get_user(scope['query_string'].decode())
        if scope['user'] is None:
            await send({
                "type": "websocket.close",
                "code": 401,
                "text": "Invalid token"
            })
            return

        return await self.inner(scope, receive, send)
