from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, BOM
from .serializers import CategorySerializer, ProductSerializer, BOMSerializer
from .filters import ProductFilter, BOMFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'code', 'description']
    ordering_fields = ['name', 'unit_price', 'updated_at']


class BOMViewSet(viewsets.ModelViewSet):
    queryset = BOM.objects.select_related('product', 'component').all()
    serializer_class = BOMSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BOMFilter
    ordering_fields = ['product__name', 'quantity']
