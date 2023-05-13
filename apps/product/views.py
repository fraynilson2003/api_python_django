from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


# Create your views here.
api_view(["POST", "GET", "PUT", "DELETE"])
class ProductView(viewsets.ModelViewSet):    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', "")
        queryset = queryset.filter(name__icontains=name)
        
        return queryset
    

