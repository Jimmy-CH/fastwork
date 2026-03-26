import django_filters
from .models import KnowledgeArticle


class KnowledgeArticleFilter(django_filters.FilterSet):
    category_id = django_filters.NumberFilter(field_name='category__id')
    is_published = django_filters.BooleanFilter(field_name='is_published')

    class Meta:
        model = KnowledgeArticle
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'tags': ['icontains'],
        }

