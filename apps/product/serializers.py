from rest_framework import serializers
from .models import Category, Product, BOM


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True, allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'


class BOMSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    component = ProductSerializer(read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    component_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='component', write_only=True)

    class Meta:
        model = BOM
        fields = '__all__'

