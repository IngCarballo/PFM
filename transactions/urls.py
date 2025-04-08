# Importamos las funciones y clases necesarias
from django.urls import path, include                         # path para definir rutas, include para incluir otras urls
from rest_framework.routers import DefaultRouter              # DefaultRouter crea automáticamente las rutas REST

# Importamos los ViewSets que definimos en views.py
from .views import MovementViewSet, CategoryViewSet

# Creamos una instancia del router de DRF
router = DefaultRouter()

# Registramos el ViewSet de movimientos con la ruta 'movements'
# basename es necesario si no se usa un queryset directamente en el viewset
router.register(r'movements', MovementViewSet, basename='movement')

# Registramos el ViewSet de categorías con la ruta 'categories'
router.register(r'categories', CategoryViewSet, basename='category')

# Definimos las rutas que esta app va a exponer
urlpatterns = [
    path('', include(router.urls)),  # Incluimos todas las rutas generadas automáticamente por el router
]
