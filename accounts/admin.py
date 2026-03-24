from django.contrib import admin
from .models import Department, Role, UserProfile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # 移除了 'created_at'
    search_fields = ('name', 'description')
    # list_filter = ('created_at',) # 移除了 'created_at' 的过滤器


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone', 'address')
    list_filter = ('department', 'role')



