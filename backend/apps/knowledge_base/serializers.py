from rest_framework import serializers
from .models import KnowledgeCategory, KnowledgeArticle


class KnowledgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeCategory
        fields = '__all__'


class KnowledgeArticleSerializer(serializers.ModelSerializer):
    category = KnowledgeCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=KnowledgeCategory.objects.all(), source='category', write_only=True)

    class Meta:
        model = KnowledgeArticle
        fields = '__all__'

