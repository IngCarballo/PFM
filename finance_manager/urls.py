from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),                        # Ruta para acceder al panel de administración de Django
    path('api/', include('transactions.urls')),             # Incluye todas las URLs de la app 'transactions' bajo el prefijo /api/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),  # tu nueva app (si usás más vistas)
]
