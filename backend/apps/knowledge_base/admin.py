from django.contrib import admin
from .models import KnowledgeCategory, KnowledgeArticle


@admin.register(KnowledgeCategory)
class KnowledgeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(KnowledgeArticle)
class KnowledgeArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_published', 'updated_at')
    list_filter = ('category', 'is_published', 'author')
    search_fields = ('title', 'tags')

