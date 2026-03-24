import django_filters
from .models import Customer, Quotation


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'name': ['exact', 'icontains'],
            'type': ['exact'],
            'phone': ['icontains'],
            'email': ['icontains'],
            'level': ['exact', 'icontains'],
        }


class QuotationFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer__id')

    class Meta:
        model = Quotation
        fields = {
            'status': ['exact'],
            'title': ['icontains'],
        }

