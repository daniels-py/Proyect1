from django.urls import path
from .views import RegisterView, EmailLoginView, ListUsersView, ProfileView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # Ruta para registrar usuarios
    path('login/', EmailLoginView.as_view(), name='login'), # Ruta para loguear el usuario
    path('list/', ListUsersView.as_view(), name='list_users'),# Nueva ruta para listar usuarios
    path('profile/', ProfileView.as_view(), name='profile'),# ruta para ver mi perfil

]