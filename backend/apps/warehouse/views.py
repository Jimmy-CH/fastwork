from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import F       # 用于过滤器中的计算
from .models import PurchaseOrder, Inventory, InventoryTransaction
from .serializers import PurchaseOrderSerializer, InventorySerializer, InventoryTransactionSerializer
from .filters import PurchaseOrderFilter, InventoryFilter, InventoryTransactionFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PurchaseOrderFilter
    search_fields = ['po_number', 'supplier']
    ordering_fields = ['created_at', 'total_amount', 'status']


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.select_related('product').all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = InventoryFilter
    search_fields = ['product__name', 'product__code']
    ordering_fields = ['product__name', 'available_quantity', 'last_updated']


class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.select_related('product').all()
    serializer_class = InventoryTransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = InventoryTransactionFilter
    search_fields = ['reference_doc', 'notes']
    ordering_fields = ['created_at', 'quantity']

