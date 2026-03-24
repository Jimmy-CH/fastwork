from rest_framework import serializers

from customer.models import Customer
from .models import MallOrder
from customer.serializers import CustomerSerializer


class MallOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)

    class Meta:
        model = MallOrder
        fields = '__all__'
        read_only_fields = ('order_number', 'created_at', 'paid_at', 'shipped_at', 'delivered_at')
