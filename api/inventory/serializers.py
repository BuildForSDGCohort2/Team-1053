from rest_framework import serializers
from .models import Stock, Tag, Product


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
