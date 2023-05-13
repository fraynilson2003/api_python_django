from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseServerError
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import check_password
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from apps.product.models import Product 
from .serializer import UserSerializer
import json
# Create your views here.
@api_view(["POST", "GET"])
def admin_usuario(request):
    if request.method == 'GET':
        try:
            username = request.GET.get('username', '') # Obtiene el valor de la clave 'username' del query, o '' si no se proporcionó
            users = User.objects.filter(username__icontains=username)
            serializer = UserSerializer(users, many=True)
            
            return JsonResponse({
                "message": "successful extraction",
                "users": serializer.data
            })
        except Exception as e:
            return JsonResponse({
                "message": str(e)
            }, status=404)         
    elif request.method == 'POST':
        try: 
            if 'application/json' in request.content_type:
                data = json.loads(request.body)
            else:
                data = request.POST
            
            username = data['username']
            email = data['email']
            password = data['password']
            
            if not username or not email or not password:
                return JsonResponse({
                    "message": "Mising data"
                }, status=404)
            
            
            User.objects.create_user(username=username, email=email, password=password)
            
            body =  {
                "username": username,
                "email": email,
                "password": password
            }
            
            return JsonResponse({
                "message": "Creado correctamente",
                "body": body
            }, safe=False )
        
        except Exception as e:
            return JsonResponse({
                "message": str(e)
            }, status=404)
            
@api_view(["POST"])
def login_user(request):
    print("*******************************************************")
    print("Entro")
    
    if 'application/json' in request.content_type:
        data = json.loads(request.body)
    else:
        data = request.POST
    
    email = data['email']
    password = data['password']
    
    user: User
    
    csrf_token = get_token(request)
    
    try:
        user = User.objects.get(email=email)
        user_serializer = UserSerializer(user)
        
    except User.DoesNotExist:
        return JsonResponse({
            "message": "El usuario no existe"
        })
    print(f" {password} ")
    pwd_valid = check_password(password, user.password)
    
    if not pwd_valid:
        return JsonResponse({
            "message": "La contraseña es invalida"
        })

    token, created = Token.objects.get_or_create(user=user)
    return JsonResponse({
        "message": "login successfully",
        "token": f"token {token.key}",
        "X-CSRFToken": csrf_token,
        **user_serializer.data
    })

#GET USER // Esta parte sirve para traer detaller de un user

# class UserDetailView(RetrieveAPIView):
#     # Define el modelo y el serializador que se van a utilizar
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

def detail_User(request, pk):
    try:
        user_detail = User.objects.get(id=pk)
        serializer = UserSerializer(user_detail)
        
        
        
        return JsonResponse({
            "message": "Details extracted successfully",
            "user": serializer.data
        })
    
    except Exception as e:
        return JsonResponse({
            "message": str(e)
        }, status=200)  

   
class ProductosUsuarioView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            idUser = request.query_params.get('userId')
            user = User.objects.get(id=idUser)
            products = user.products.all()
            data = list(products.values())
            return JsonResponse({
                "message": "success",
                "products": data
            }, status=202)
        except User.DoesNotExist:
            return JsonResponse({
                "message": "El usuario no existe"
            }, status=404)
        except Exception as e:
            return JsonResponse({
                "message": str(e)
            }, status=400)

@api_view(["POST", "GET"])
def admin_Product(request, idPro):
    permission_classes = [IsAuthenticated]

    if request.method == 'POST':
        try:
            if 'application/json' in request.content_type:
                data = json.loads(request.body)
            else:
                data = request.POST
            
            user_id = data['userId']

            
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=idPro)

            user.products.add(product)
            return JsonResponse({
                "message": "Product added successfully"
            })
        except Exception as e:
            return JsonResponse({
                "message": str(e)
            }, status=200)
      
    elif request.method == 'DELETE':
        print("*******************************************************")
        print("Entro al Delete")
        try:
            user = User.objects.get(id=3)
            product = Product.objects.get(id=idPro)
            
            ##Para elinar todo
            #user.products.clear()
            user.products.remove(product)  
            
            return JsonResponse({
                "message": "Deleted successfully"
            })
        except Exception as e:
            return JsonResponse({
                "message": str(e)
            }, status=200)
    
                

            
    return JsonResponse({
            "message": "Salio mallllll22222"
    })
