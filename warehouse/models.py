from django.db import models
from product.models import Product


class PurchaseOrder(models.Model):
    PO_STATUS_CHOICES = [
        ('draft', '草稿'),
        ('submitted', '已提交'),
        ('approved', '已审批'),
        ('received', '已收货'),
        ('cancelled', '已取消'),
    ]
    po_number = models.CharField(max_length=50, unique=True, verbose_name="采购单号")
    supplier = models.CharField(max_length=100, verbose_name="供应商")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="总金额")
    status = models.CharField(max_length=20, choices=PO_STATUS_CHOICES, default='draft', verbose_name="状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    approved_at = models.DateTimeField(null=True, blank=True, verbose_name="审批时间")
    received_at = models.DateTimeField(null=True, blank=True, verbose_name="收货时间")

    def __str__(self):
        return self.po_number

    class Meta:
        verbose_name = "采购订单"
        verbose_name_plural = "采购订单"


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="产品")
    quantity_on_hand = models.IntegerField(default=0, verbose_name="现有库存")
    quantity_reserved = models.IntegerField(default=0, verbose_name="预留库存")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    @property
    def available_quantity(self):
        """可用库存 = 现有库存 - 预留库存"""
        return self.quantity_on_hand - self.quantity_reserved

    def __str__(self):
        return f"{self.product.name}: {self.available_quantity}"

    class Meta:
        verbose_name = "库存"
        verbose_name_plural = "库存"


class InventoryTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('in', '入库'),
        ('out', '出库'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="产品")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, verbose_name="交易类型")
    quantity = models.IntegerField(verbose_name="数量")
    reference_doc = models.CharField(max_length=100, verbose_name="关联单据") # 如: 工单号, 采购单号
    notes = models.TextField(blank=True, verbose_name="备注")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="交易时间")

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.product.name}"

    class Meta:
        verbose_name = "库存流水"
        verbose_name_plural = "库存流水"

