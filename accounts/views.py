from rest_framework import generics
from .serializers import RegisterSerializer
from accounts.models import User  # Cambiar la importación al modelo personalizado
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema  # Importa extend_schema para documentar la vista

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

@extend_schema(
    summary="Actualizar el rol del usuario",
    description="Permite a un usuario autenticado actualizar su rol.",
    request={
        "application/json": {
            "example": {
                "rol": "nuevo_rol"
            }
        }
    },
    responses={
        200: {
            "description": "Rol actualizado correctamente.",
            "example": {
                "message": "Rol actualizado correctamente.",
                "rol": "nuevo_rol"
            }
        },
        400: {
            "description": "Error en la solicitud.",
            "example": {
                "error": "El campo 'rol' es obligatorio."
            }
        }
    }
)
class UpdateUserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        new_role = request.data.get('rol')

        if not new_role:
            return Response({"error": "El campo 'rol' es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

        user.rol = new_role
        user.save()
        return Response({"message": "Rol actualizado correctamente.", "rol": user.rol}, status=status.HTTP_200_OK)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "role": user.rol,
    })