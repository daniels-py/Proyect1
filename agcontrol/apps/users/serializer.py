from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers

from django.contrib.auth import authenticate



User = get_user_model() # obtenemos el modelo de usuario personalizado

class UserSeralizer(serializers.ModelSerializer):
    
    # validacion estra para confirmar la contraseña
    password2 = serializers.CharField(write_only=True) # solo se utiliz para confirmar la contraseña

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name','last_name', 'email', 'phone_number', 'password', 'password2']
        extra_kwargs = { # evita que el password se muestre en las respuestas
            'password': {'write_only': True} # la contraseña solo se puede escribir, no leer
        }
        #funcion que valida que las contraseñas coincidan y crea el usuario
        def validate(self, data):
            if data ['password'] != data['password2']: # validamos si las contraseñas coinciden
                raise serializers.ValidationError("Las contraseñas no coinciden") # si no coinciden, lanzamos un error
            return data # si coinciden, retornamos los datos
        
        #funcion que crea el usuario con los datos validados  
        def create(self, validated_data):
            validated_data.pop('password2') # eliminamos password2 ya que no es necesario para crear el usuario
            
            # creamos el usuario utilizando el metodo create_user del modelo User
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                phone_number=validated_data.get('phone_number', ''), # si no se proporciona, se asigna una cadena vacía
                role=validated_data['role'],
                password=validated_data['password']
            )
            return user
        

class EmailLoginTokenSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD   
    #funcion para valida el correo y contraña existentes del usuaurio
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password

        )
        user = authenticate(request=self.context.get('request'), email=email, password=password)

        #validacion en caso de que los datos esten mal 
        if not user:
            raise serializers.ValidationError("Credenciales invalidas, verifica tu correo contraseña. ")
        
        # Continuamos con al generacion del token

        data = super().validate(attrs)
        data['user'] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }

        return data 