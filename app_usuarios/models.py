from django.db import models

# Create your models here.
# Tabla clase Usuario
class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=150, unique=True) # Nombre de usuario único
    email = models.EmailField(unique=True) # Correo electrónico único
    nombre = models.CharField(max_length=100, blank=True, null=True) # Nombre real del usuario
    apellido = models.CharField(max_length=100, blank=True, null=True) # Apellido del usuario
    is_activo = models.BooleanField(default=True) # Indica si la cuenta está activa
    ultima_conexion = models.DateTimeField(blank=True, null=True) # Última vez que el usuario inició sesión

    def __str__(self):
        return f"{self.nombre_usuario} {self.email}"