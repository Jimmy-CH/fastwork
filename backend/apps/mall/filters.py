import django_filters
from .models import MallOrder


class MallOrderFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer__id')

    class Meta:
        model = MallOrder
        fields = {
            'order_number': ['icontains'],
            'status': ['exact'],
            'total_amount': ['gte', 'lte'],
        }
