from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # crea la sesión y guarda cookie
            return Response({"message": "Sesión iniciada correctamente"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "Sesión cerrada"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No hay sesión activa"}, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
    })