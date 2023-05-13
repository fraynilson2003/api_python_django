from apps.product.models import Product 
from rest_framework import serializers
from apps.product.serializer import ProductSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    #products = serializers.SerializerMethodField()

    # Define los campos que deseas incluir en la representación del modelo
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions"
        ]
        #exclude = ['password']


    # def get_products(self, obj):
    #     queryset = Product.objects.filter(users=obj)
    #     serializer = ProductSerializer(queryset, many=True)
        
    #     return serializer.data
        