from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r"category", views.CategoryView, "Category")


urlpatterns = [
    path("api/", include(router.urls))
]