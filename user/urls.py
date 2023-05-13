from django.urls import path, include
from . import views
from django.urls import path, include

urlpatterns = [
    path('api/user/<int:pk>/', views.detail_User, name='user-detail'),

    path("api/user", views.admin_usuario, name='admin_usuario'),

    path("api/user/admin_product", views.ProductosUsuarioView.as_view(), name='get_products_user'),
    path("api/user/admin_product/<int:idPro>", views.admin_Product, name='admin_Product'),

    path("api/user/login", views.login_user, name='login_user'),
]

