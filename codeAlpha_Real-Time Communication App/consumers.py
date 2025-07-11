import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "global"
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data['username']
        content = data['message']

        message = Message.objects.create(username=username, content=content)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': content,
                'timestamp': str(datetime.now().strftime("%H:%M:%S"))
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
