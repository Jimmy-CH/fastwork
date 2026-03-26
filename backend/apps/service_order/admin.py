from django.contrib import admin
from .models import WorkOrder, Feedback


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'priority', 'assigned_to', 'updated_at')
    list_filter = ('status', 'priority', 'assigned_to')
    search_fields = ('title', 'description')
    raw_id_fields = ('customer', 'assigned_to')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('work_order', 'satisfaction_rating', 'created_at')
    raw_id_fields = ('work_order',)
