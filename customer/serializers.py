from rest_framework import serializers
from .models import Customer, Quotation


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class QuotationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)

    class Meta:
        model = Quotation
        fields = '__all__'

