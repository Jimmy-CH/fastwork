from rest_framework import serializers

from product.models import Product
from .models import PurchaseOrder, Inventory, InventoryTransaction
from product.serializers import ProductSerializer


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ('quantity_on_hand', 'last_updated') # 这些字段通常不由用户直接修改


class InventoryTransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = InventoryTransaction
        fields = '__all__'
        read_only_fields = ('created_at',)

