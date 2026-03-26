from rest_framework import serializers

from apps.accounts.models import UserProfile
from .models import Message
from apps.accounts.serializers import UserProfileSerializer


class MessageSerializer(serializers.ModelSerializer):
    recipient_user = UserProfileSerializer(read_only=True)
    recipient_user_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='recipient_user', write_only=True, allow_null=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created_at',)

