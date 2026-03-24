from rest_framework import serializers

from accounts.models import UserProfile
from customer.models import Customer
from .models import WorkOrder, Feedback
from customer.serializers import CustomerSerializer
from accounts.serializers import UserProfileSerializer


class WorkOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    assigned_to = UserProfileSerializer(read_only=True)

    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='assigned_to', write_only=True, allow_null=True)

    class Meta:
        model = WorkOrder
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer(read_only=True)
    work_order_id = serializers.PrimaryKeyRelatedField(queryset=WorkOrder.objects.all(), source='work_order', write_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'

