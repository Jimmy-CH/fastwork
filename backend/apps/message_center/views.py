from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from .filters import MessageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related('recipient_user').all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MessageFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'is_read']

