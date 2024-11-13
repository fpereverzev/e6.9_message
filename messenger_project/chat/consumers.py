import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Подключаем пользователя к группе чата
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(f"User connected to room: {self.room_name}")

        # Принимаем подключение
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаем пользователя от группы чата
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"User disconnected from room: {self.room_name}")

    async def receive(self, text_data):
        # Получаем сообщение от клиента
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f"Message received: {message}")

        # Отправляем сообщение всем участникам группы чата
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Отправляем сообщение обратно клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
