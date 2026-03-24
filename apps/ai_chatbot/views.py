from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from .filters import ChatSessionFilter, ChatMessageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ChatSessionViewSet(viewsets.ModelViewSet):
    queryset = ChatSession.objects.select_related('customer').all()
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ChatSessionFilter
    search_fields = ['session_id', 'customer__name']
    ordering_fields = ['created_at', 'last_interaction_at']


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.select_related('session').all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ChatMessageFilter
    ordering_fields = ['timestamp']

