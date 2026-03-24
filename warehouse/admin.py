from django.contrib import admin
from .models import PurchaseOrder, Inventory, InventoryTransaction


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'supplier', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_on_hand', 'quantity_reserved', 'available_quantity', 'last_updated')
    raw_id_fields = ('product',)
    readonly_fields = ('available_quantity',)


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'transaction_type', 'quantity', 'reference_doc', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    raw_id_fields = ('product',)

