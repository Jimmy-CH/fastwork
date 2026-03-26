from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WorkOrder, Feedback
from .serializers import WorkOrderSerializer, FeedbackSerializer
from .filters import WorkOrderFilter, FeedbackFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.select_related('customer', 'assigned_to').all()
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WorkOrderFilter
    search_fields = ['title', 'description', 'customer__name']
    ordering_fields = ['created_at', 'updated_at', 'priority', 'status']


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.select_related('work_order').all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FeedbackFilter
    ordering_fields = ['created_at', 'satisfaction_rating']

