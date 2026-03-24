from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Quotation
from .serializers import CustomerSerializer, QuotationSerializer
from .filters import CustomerFilter, QuotationFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomerFilter
    search_fields = ['name', 'contact_person', 'address']
    ordering_fields = ['name', 'created_at', 'credit_score']


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.select_related('customer').all()
    serializer_class = QuotationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = QuotationFilter
    search_fields = ['title', 'customer__name']
    ordering_fields = ['created_at', 'total_amount']


