import django_filters
from .models import PurchaseOrder, Inventory, InventoryTransaction


class PurchaseOrderFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrder
        fields = {
            'po_number': ['icontains'],
            'supplier': ['icontains'],
            'status': ['exact'],
            'total_amount': ['gte', 'lte'],
        }


class InventoryFilter(django_filters.FilterSet):
    product_id = django_filters.NumberFilter(field_name='product__id')
    min_stock_threshold = django_filters.NumberFilter(method='filter_low_stock')

    class Meta:
        model = Inventory
        fields = []

    def filter_low_stock(self, queryset, name, value):
        """过滤库存低于设定阈值的商品"""
        return queryset.filter(product__min_stock__gt=0).filter(quantity_on_hand__lt=F('product__min_stock'))


class InventoryTransactionFilter(django_filters.FilterSet):
    product_id = django_filters.NumberFilter(field_name='product__id')
    transaction_type = django_filters.CharFilter(field_name='transaction_type')

    class Meta:
        model = InventoryTransaction
        fields = {
            'reference_doc': ['icontains'],
        }

