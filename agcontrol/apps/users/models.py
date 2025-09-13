from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # esto es uan tupla para asignar roles a los usuarios
    ROLE_CHOICES=(
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    # estos campos son para el modelo de usuario
    # email es unico y obligatorio
    email = models.EmailField(unique=True)
    # el telefono es opcional pero unico cuando se ingresa
    phone_number = models.CharField(max_length=15, blank=True)
    # el rol es obligatorio y por defecto es user para los demas usuarios
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    #sirve para dar una representación legible del objeto User utili para ver en el admin
    def __str__(self):
        return f"{self.username} - {self.email}"