from django.shortcuts import render
from .models import Message, ChatGroup
from rest_framework import viewsets
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
    # Получение всех сообщений для данной комнаты
    messages = Message.objects.filter(chat_group__name=room_name)

    # Проверка существования группы чата
    try:
        chat_group = ChatGroup.objects.get(name=room_name)
    except ChatGroup.DoesNotExist:
        chat_group = None

    # Передаем в контекст данные о комнате, сообщениях и группе чата
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'messages': messages,
        'chat_group': chat_group,
    })
