from django.db import models
from apps.customer.models import Customer
from apps.accounts.models import UserProfile


class WorkOrder(models.Model):
    PRIORITY_CHOICES = [
        (1, '低'),
        (2, '中'),
        (3, '高'),
        (4, '紧急'),
    ]
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('assigned', '已分配'),
        ('in_progress', '处理中'),
        ('completed', '已完成'),
        ('closed', '已关闭'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="客户")
    title = models.CharField(max_length=200, verbose_name="工单标题")
    description = models.TextField(verbose_name="问题描述")
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2, verbose_name="优先级")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="状态")
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="指派给")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return f"[{self.get_status_display()}] {self.title}"

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = "工单"


class Feedback(models.Model):
    work_order = models.OneToOneField(WorkOrder, on_delete=models.CASCADE, verbose_name="关联工单")
    satisfaction_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="满意度评分")
    comments = models.TextField(verbose_name="反馈意见")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")

    def __str__(self):
        return f"工单 {self.work_order.id} 的反馈"

    class Meta:
        verbose_name = "客户反馈"
        verbose_name_plural = "客户反馈"


