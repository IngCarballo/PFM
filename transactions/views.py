from rest_framework import viewsets, permissions
from .models import Movement, Category
from .serializers import MovementSerializer, CategorySerializer

class MovementViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre movimientos.
    """
    serializer_class = MovementSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios logueados pueden acceder

    def get_queryset(self):
        # Filtramos los movimientos para que el usuario solo vea los suyos
        return Movement.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Asignamos el usuario automáticamente cuando se crea un movimiento
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre categorías.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Si las categorías son compartidas por todos los usuarios, devolvemos todas.
        return Category.objects.all()
