from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterView, current_user, UpdateUserRoleView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# Sin usar router para estas views "manuales"
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('me/', current_user, name='current_user'),
#     path('update-role/', UpdateUserRoleView.as_view(), name='update-role'),
# ]
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('me/', current_user, name='current_user'),
    path('update-role/', UpdateUserRoleView.as_view(), name='update-role'),
]