from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MallOrder
from .serializers import MallOrderSerializer
from .filters import MallOrderFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class MallOrderViewSet(viewsets.ModelViewSet):
    queryset = MallOrder.objects.select_related('customer').all()
    serializer_class = MallOrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MallOrderFilter
    search_fields = ['order_number', 'shipping_address', 'customer__name']
    ordering_fields = ['created_at', 'total_amount', 'status']

