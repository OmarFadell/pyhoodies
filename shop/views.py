from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q

@api_view(['GET'])
def product_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)
