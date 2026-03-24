from django.db import models
from apps.accounts.models import UserProfile


class Message(models.Model):
    TYPE_CHOICES = [
        ('notification', '通知'),
        ('alert', '告警'),
        ('reminder', '提醒'),
    ]
    recipient_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="接收人", null=True, blank=True)
    recipient_group = models.CharField(max_length=100, verbose_name="接收组", blank=True) # 如: '技术部', '客服组'
    message_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="消息类型")
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    is_read = models.BooleanField(default=False, verbose_name="是否已读")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = "消息"


