from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="部门名称")
    description = models.TextField(blank=True, verbose_name="描述")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"


class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name="角色名称")
    permissions = models.JSONField(default=list, verbose_name="权限列表") # 示例: ["view_customer", "edit_workorder"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="所属部门")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="角色")

    def __str__(self):
        return f"{self.user.username} - {self.role.name if self.role else '无角色'}"

    class Meta:
        verbose_name = "用户档案"
        verbose_name_plural = "用户档案"
