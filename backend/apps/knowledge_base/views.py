from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import KnowledgeCategory, KnowledgeArticle
from .serializers import KnowledgeCategorySerializer, KnowledgeArticleSerializer
from .filters import KnowledgeArticleFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class KnowledgeCategoryViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeCategory.objects.all()
    serializer_class = KnowledgeCategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']


class KnowledgeArticleViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeArticle.objects.select_related('category').all()
    serializer_class = KnowledgeArticleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = KnowledgeArticleFilter
    search_fields = ['title', 'content', 'tags', 'author']
    ordering_fields = ['created_at', 'updated_at', 'author']

