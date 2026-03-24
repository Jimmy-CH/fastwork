from django.contrib import admin
from .models import Department, Role, UserProfile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role')
    list_filter = ('department', 'role')
    raw_id_fields = ('user',)

