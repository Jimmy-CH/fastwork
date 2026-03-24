from django.contrib import admin
from .models import MallOrder


@admin.register(MallOrder)
class MallOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    raw_id_fields = ('customer',)
    readonly_fields = ('items',)

