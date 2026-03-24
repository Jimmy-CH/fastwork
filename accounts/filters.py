import django_filters
from .models import UserProfile


class UserProfileFilter(django_filters.FilterSet):
    department_id = django_filters.NumberFilter(field_name='department__id')
    role_id = django_filters.NumberFilter(field_name='role__id')

    class Meta:
        model = UserProfile
        fields = {
            'user__username': ['exact', 'icontains'],
            'user__first_name': ['icontains'],
            'user__last_name': ['icontains'],
        }

