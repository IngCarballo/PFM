from rest_framework import viewsets, permissions
from .models import Movement, Category
from .serializers import MovementSerializer, CategorySerializer
from django.db.models import Q

class MovementViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre movimientos.
    """
    serializer_class = MovementSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def get_queryset(self):
        """
        Filtra los movimientos para que el usuario solo vea los suyos.
        """
        user = self.request.user
        if user.is_superuser:
            return Movement.objects.all().order_by('-date')  # Los superusuarios ven todo
        return Movement.objects.filter(user=user).order_by('-date')  # Solo movimientos del usuario

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario al crear un movimiento.
        """
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre categorías.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def get_queryset(self):
        """
        Filtra las categorías para que el usuario solo vea las suyas y las globales.
        """
        user = self.request.user
        if user.is_superuser:
            return Category.objects.all().order_by('name')  # Los superusuarios ven todo
        return Category.objects.filter(Q(user=user) | Q(user__isnull=True)).order_by('name')  # Categorías propias y globales

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario al crear una categoría.
        """
        serializer.save(user=self.request.user)