from django.db import models


class KnowledgeCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    description = models.TextField(blank=True, verbose_name="描述")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "知识库分类"
        verbose_name_plural = "知识库分类"


class KnowledgeArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.CharField(max_length=200, blank=True, verbose_name="标签") # 逗号分隔
    author = models.CharField(max_length=100, verbose_name="作者")
    is_published = models.BooleanField(default=False, verbose_name="是否发布")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "知识库文章"
        verbose_name_plural = "知识库文章"


