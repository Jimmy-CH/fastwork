from django.contrib import admin
from .models import Customer, Quotation


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contact_person', 'phone', 'level', 'credit_score', 'created_at')
    list_filter = ('type', 'level')
    search_fields = ('name', 'contact_person', 'phone')


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    raw_id_fields = ('customer',)

