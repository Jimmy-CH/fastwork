from django.db import models
from customer.models import Customer
from product.models import Product


class MallOrder(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending_payment', '待支付'),
        ('paid', '已支付'),
        ('shipped', '已发货'),
        ('delivered', '已送达'),
        ('cancelled', '已取消'),
    ]
    order_number = models.CharField(max_length=50, unique=True, verbose_name="订单号")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="客户")
    items = models.JSONField(verbose_name="订单项") # 示例: [{"product_id": 1, "quantity": 2, "price": 99.9}]
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="总金额")
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending_payment', verbose_name="状态")
    shipping_address = models.TextField(verbose_name="收货地址")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    shipped_at = models.DateTimeField(null=True, blank=True, verbose_name="发货时间")
    delivered_at = models.DateTimeField(null=True, blank=True, verbose_name="送达时间")

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "商城订单"
        verbose_name_plural = "商城订单"

