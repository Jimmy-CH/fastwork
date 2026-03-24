from django.contrib import admin
from .models import ChatSession, ChatMessage


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'customer', 'created_at', 'last_interaction_at')
    raw_id_fields = ('customer',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'role', 'timestamp')
    list_filter = ('role', 'timestamp')
    raw_id_fields = ('session',)
    readonly_fields = ('content',)
