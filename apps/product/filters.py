import django_filters
from .models import Product, BOM


class ProductFilter(django_filters.FilterSet):
    category_id = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'code': ['icontains'],
            'unit_price': ['gte', 'lte'],
        }


class BOMFilter(django_filters.FilterSet):
    product_id = django_filters.NumberFilter(field_name='product__id')
    component_id = django_filters.NumberFilter(field_name='component__id')

    class Meta:
        model = BOM
        fields = []
