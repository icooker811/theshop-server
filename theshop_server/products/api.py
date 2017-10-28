from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from recommenders.functions import *


@api_view(['GET'])
def product_list(request):

    q = request.query_params.get('q') or ''
    if q:
        price = request.query_params.get('price') or 1000.0
        queryset = get_product_recommendation(q, price=price)
    else:
        queryset = Product.objects.all().order_by('name')[:3]

    serializer = ProductSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
