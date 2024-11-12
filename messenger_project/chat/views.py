from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, ChatGroup
from .serializers import MessageSerializer, ChatGroupSerializer
from rest_framework.permissions import IsAuthenticated

# Viewset для сообщений
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

# Viewset для групповых чатов
class ChatGroupViewSet(viewsets.ModelViewSet):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer
    permission_classes = [IsAuthenticated]

# View для рендеринга страницы чата
def chat_room(request, room_name):
    return render(request, 'chat/chat_room.html', {'room_name': room_name})
