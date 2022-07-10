"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import chat_app.routing
from chat_app.middlewares import QueryAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        QueryAuthMiddleware(
            URLRouter(
                chat_app.routing.websocket_urlpatterns,
            ),
        ),
    ),
})

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 chat_app.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })