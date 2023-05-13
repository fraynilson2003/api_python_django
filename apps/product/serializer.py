from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Product
        fields = [
        "id",
        "name",
        "photo",
        "description",
        "price",
        "category",
        "quantity",
        "date_created",   
        "users"
        ]
        