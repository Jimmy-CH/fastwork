from rest_framework import serializers

from customer.models import Customer
from .models import ChatSession, ChatMessage
from customer.serializers import CustomerSerializer


class ChatSessionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True, allow_null=True)

    class Meta:
        model = ChatSession
        fields = '__all__'
        read_only_fields = ('session_id', 'created_at', 'last_interaction_at')


class ChatMessageSerializer(serializers.ModelSerializer):
    session = ChatSessionSerializer(read_only=True)
    session_id = serializers.PrimaryKeyRelatedField(queryset=ChatSession.objects.all(), source='session', write_only=True)

    class Meta:
        model = ChatMessage
        fields = '__all__'
        read_only_fields = ('timestamp',)

