import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    recipient_user_id = django_filters.NumberFilter(field_name='recipient_user__id')

    class Meta:
        model = Message
        fields = {
            'message_type': ['exact'],
            'is_read': ['exact'],
            'title': ['icontains'],
        }

