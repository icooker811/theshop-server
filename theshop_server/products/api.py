from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.all().order_by('name')[:10]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
