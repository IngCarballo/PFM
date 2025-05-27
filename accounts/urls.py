from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, current_user, UpdateUserRoleView

# Sin usar router para estas views "manuales"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', current_user, name='current_user'),
    path('update-role/', UpdateUserRoleView.as_view(), name='update-role'),
]
