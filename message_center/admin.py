from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient_user', 'recipient_group', 'message_type', 'is_read', 'created_at')
    list_filter = ('message_type', 'is_read', 'created_at')
    raw_id_fields = ('recipient_user',)

