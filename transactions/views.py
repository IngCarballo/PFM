from rest_framework import viewsets, permissions
from .models import Movement, Category
from .serializers import MovementSerializer, CategorySerializer
from django.db.models import Q

class MovementViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre movimientos.
    """
    serializer_class = MovementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Movement.objects.all().order_by('-date')
        # Filtramos los movimientos para que el usuario solo vea los suyos
        return Movement.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Asignamos el usuario automáticamente al crear un movimiento
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre categorías.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Category.objects.all().order_by('name')
        # Solo las categorías propias del usuario y las globales (user=None)
        return Category.objects.filter(Q(user=user) | Q(user__isnull=True)).order_by('name')

    def perform_create(self, serializer):
        # Asignamos automáticamente el usuario que crea la categoría
        serializer.save(user=self.request.user)