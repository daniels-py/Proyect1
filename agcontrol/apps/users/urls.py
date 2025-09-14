from django.urls import path
from .views import RegisterView, EmailLoginView, ListUsersView, ProfileView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # Ruta para registrar usuarios
    path('login/', EmailLoginView.as_view(), name='login'), # Ruta para loguear el usuario
    path('logout/', LogoutView.as_view(), name='logout'), # Ruta para cerrar sesion

    path('list/', ListUsersView.as_view(), name='list_users'),# Nueva ruta para listar usuarios
    path('profile/', ProfileView.as_view(), name='profile'),# ruta para ver mi perfil

]