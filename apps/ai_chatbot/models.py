from django.db import models
from apps.customer.models import Customer


class ChatSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True, verbose_name="会话ID")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="关联客户", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    last_interaction_at = models.DateTimeField(auto_now=True, verbose_name="最后互动时间")

    def __str__(self):
        return f"Chat with {self.customer.name if self.customer else 'Guest'}"

    class Meta:
        verbose_name = "AI对话会话"
        verbose_name_plural = "AI对话会话"


class ChatMessage(models.Model):
    ROLE_CHOICES = [
        ('user', '用户'),
        ('assistant', 'AI助手'),
    ]
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages', verbose_name="会话")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name="角色")
    content = models.TextField(verbose_name="消息内容")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="时间戳")

    def __str__(self):
        return f"{self.role}: {self.content[:50]}..."

    class Meta:
        verbose_name = "AI对话消息"
        verbose_name_plural = "AI对话消息"

