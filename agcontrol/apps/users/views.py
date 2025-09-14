from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import permissions

from rest_framework.response import Response


from rest_framework.views import APIView

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


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # se define el metodo get para poder obtener los datos del usuario autentificado
    def get (self, request):
        """
        explicacion propia por mi
        obtenemos el usuario autentificado con ('request.user')
        devulve los datos del usuario en el formato JSN.
        agregamos un mensaje de bienvenida personalizado
        """
        user = request.user #aqui obtenemos el usuario
        # retornara los siguientes datos de la solciitud
        return Response({
            "message":f"¡Bienvenido!, {user.username} ! ",
            "id": user.id,
            "username": user.username,
            "email": user.email,
            'phone_number': user.phone_number,
            'role': user.role
        })