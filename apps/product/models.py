from django.db import models
from datetime import datetime
from apps.category.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)
    users = models.ManyToManyField(User, related_name='products', blank=True)

    def __str__(self)->str:
        return self.name
    
