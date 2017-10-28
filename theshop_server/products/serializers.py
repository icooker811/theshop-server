from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    pid = serializers.CharField()
    product_name = serializers.CharField()
    product_url = serializers.CharField()
    retail_price = serializers.FloatField()
    discounted_price = serializers.FloatField()
    first_image = serializers.CharField()
