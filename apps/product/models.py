from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="上级分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品分类"
        verbose_name_plural = "产品分类"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="产品名称")
    code = models.CharField(max_length=50, unique=True, verbose_name="产品编码")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="分类")
    description = models.TextField(blank=True, verbose_name="产品描述")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="成本价")
    unit = models.CharField(max_length=20, default='个', verbose_name="单位")
    min_stock = models.IntegerField(default=0, verbose_name="最低库存")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"


class BOM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bom_assemblies', verbose_name="父产品")
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bom_components', verbose_name="子组件")
    quantity = models.FloatField(verbose_name="数量")

    def __str__(self):
        return f"{self.product.name} -> {self.quantity} x {self.component.name}"

    class Meta:
        verbose_name = "BOM清单"
        verbose_name_plural = "BOM清单"


