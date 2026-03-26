import django_filters
from .models import ChatSession, ChatMessage


class ChatSessionFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer__id')

    class Meta:
        model = ChatSession
        fields = []


class ChatMessageFilter(django_filters.FilterSet):
    session_id = django_filters.NumberFilter(field_name='session__id')
    role = django_filters.CharFilter(field_name='role')

    class Meta:
        model = ChatMessage
        fields = []

