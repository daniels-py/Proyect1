from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import UserSeralizer, EmailLoginTokenSerializer

from rest_framework import generics
# Create your views here.

User = get_user_model() # obtenemos el modelo de usuario personalizado

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() # obtenemos todos los usuarios
    serializer_class = UserSeralizer # utilizamos el serializador definido en serializer.py


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all() # obtenemos todos los usuarios
    serializer_class = UserSeralizer # utilizamos el serializador definido en serializer.py


class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailLoginTokenSerializer