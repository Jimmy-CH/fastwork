import django_filters
from .models import WorkOrder, Feedback


class WorkOrderFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer__id')
    assigned_to_id = django_filters.NumberFilter(field_name='assigned_to__id')

    class Meta:
        model = WorkOrder
        fields = {
            'status': ['exact'],
            'priority': ['exact'],
            'title': ['icontains'],
        }


class FeedbackFilter(django_filters.FilterSet):
    work_order_id = django_filters.NumberFilter(field_name='work_order__id')

    class Meta:
        model = Feedback
        fields = {
            'satisfaction_rating': ['exact', 'gte', 'lte'],
        }

