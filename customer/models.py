from django.db import models


class Customer(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('individual', '个人'),
        ('enterprise', '企业'),
    ]
    name = models.CharField(max_length=100, verbose_name="客户名称")
    type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES, default='enterprise', verbose_name="客户类型")
    contact_person = models.CharField(max_length=100, verbose_name="联系人")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    email = models.EmailField(blank=True, verbose_name="邮箱")
    address = models.TextField(blank=True, verbose_name="地址")
    level = models.CharField(max_length=20, default='普通', verbose_name="客户等级")
    credit_score = models.IntegerField(default=100, verbose_name="信用分")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"


class Quotation(models.Model):
    QUOTATION_STATUS_CHOICES = [
        ('draft', '草稿'),
        ('sent', '已发送'),
        ('confirmed', '已确认'),
        ('rejected', '已拒绝'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="关联客户")
    title = models.CharField(max_length=200, verbose_name="报价单标题")
    content = models.TextField(verbose_name="报价内容")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="总金额")
    status = models.CharField(max_length=20, choices=QUOTATION_STATUS_CHOICES, default='draft', verbose_name="状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name="发送时间")
    confirmed_at = models.DateTimeField(null=True, blank=True, verbose_name="确认时间")

    def __str__(self):
        return f"{self.title} - {self.customer.name}"

    class Meta:
        verbose_name = "报价单"
        verbose_name_plural = "报价单"

