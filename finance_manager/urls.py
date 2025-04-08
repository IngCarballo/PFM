# Importamos funciones necesarias para manejar rutas
from django.contrib import admin                           # Admin de Django
from django.urls import path, include                      # path para definir rutas, include para incluir otras urls

# Lista de rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),                       # Ruta para acceder al panel de administración de Django
    path('api/', include('movements.urls')),               # Incluye todas las URLs de la app 'movements' bajo el prefijo /api/
]
