from django.db import models


class SystemConfig(models.Model):
    key = models.CharField(max_length=100, unique=True, verbose_name="配置键")
    value = models.TextField(verbose_name="配置值")
    description = models.TextField(blank=True, verbose_name="描述")

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "系统配置"
        verbose_name_plural = "系统配置"

