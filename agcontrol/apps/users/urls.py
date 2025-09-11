from django.urls import path
from .views import RegisterView, ListUsersView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # Ruta para registrar usuarios
    path('list/', ListUsersView.as_view(), name='list_users'),  # Nueva ruta para listar usuarios
]