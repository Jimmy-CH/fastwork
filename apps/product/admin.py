from django.contrib import admin
from .models import Category, Product, BOM


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category', 'unit_price', 'min_stock', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'code')


@admin.register(BOM)
class BOMAdmin(admin.ModelAdmin):
    list_display = ('product', 'component', 'quantity')
    raw_id_fields = ('product', 'component')

