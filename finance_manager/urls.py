from django.contrib import admin
from django.urls import path, include  # `include` permite traer las rutas definidas en otras apps
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Lista de rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),                        # Ruta para acceder al panel de administración de Django
    path('api/', include('transactions.urls')),             # Incluye todas las URLs de la app 'transactions' bajo el prefijo /api/
    path('api/accounts/', include('accounts.urls')),  
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
