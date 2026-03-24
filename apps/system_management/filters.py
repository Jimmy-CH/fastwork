import django_filters
from .models import SystemConfig


class SystemConfigFilter(django_filters.FilterSet):
    class Meta:
        model = SystemConfig
        fields = {
            'key': ['exact', 'icontains'],
            'description': ['icontains'],
        }

