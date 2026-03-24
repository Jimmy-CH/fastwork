from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SystemConfig
from .serializers import SystemConfigSerializer
from .filters import SystemConfigFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class SystemConfigViewSet(viewsets.ModelViewSet):
    queryset = SystemConfig.objects.all()
    serializer_class = SystemConfigSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SystemConfigFilter
    search_fields = ['key', 'description']
    ordering_fields = ['key', 'id']

