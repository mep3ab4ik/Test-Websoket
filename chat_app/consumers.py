import logging
from datetime import datetime

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from.models import Room, Message
from account_app.models import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ChatConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = None
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        self.user = self.scope['user']

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        # self.room_group_name = 'chat_%s' % self.room_name

        # Join room groups
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()



        logger.info(f'User {self.user} connected to room {self.room_name}')
        await self.send_json({
            'message': f'You have connected to the chat as {self.user.username}'
        })

    async def disconnect(self, close_code):
        # Leave the channels
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Receive messages from Websocket
    async def receive_json(self, content, **kwargs):
        message = content['message']

        # Send a message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user,
            },
        )

    # Receive messages from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to Websocket
        await self.send_json({
            'datetime': datetime.utcnow().isoformat(),
            'message': message,
            'user': user.username,
        })

    # Receive messages from room group
    async def friendship_created(self, event):
        friendship = event['friendship']


        # Send message to Websocket
        await self.send_json({
            'datetime': datetime.utcnow().isoformat(),
            'message': f'Friendship requested from {friendship.user.username} to {friendship.friend.username}',
        })

    # @database_sync_to_async
    # def add_user_to_room(self):
    #     user: User = self.user
    #     try:
    #         room = Room.objects.get(name=self.room_name)
    #         user.current_user.add(room)
    #
