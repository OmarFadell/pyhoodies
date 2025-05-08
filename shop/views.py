from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)
