from django.contrib import admin
from django.urls import path, include  # `include` permite traer las rutas definidas en otras apps

# Lista de rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),                        # Ruta para acceder al panel de administración de Django
    path('api/', include('transactions.urls')),             # Incluye todas las URLs de la app 'transactions' bajo el prefijo /api/
]
