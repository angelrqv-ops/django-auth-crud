from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    usuario_principal = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1 si es usuario que presta servicio - 2 si es usuario que requeire servicio
    tipo_usuario = models.IntegerField()

class Services(models.Model):
    nombre_servicio = models.CharField(max_length=100)

class subServices(models.Model):
    id_servicio = models.ForeignKey(Services, on_delete=models.CASCADE)
    nombre_subservicio = models.CharField(max_length=100)

class UserService(models.Model):
    nombre_completo = models.CharField(max_length=200)
    email = models.CharField(max_length=70)
    telefono = models.CharField(max_length=30)
    servicio_principal = models.ForeignKey(Services, on_delete=models.CASCADE)
    experiencia = models.TextField()

class AditionalServices(models.Model):
    user_services = models.ForeignKey(UserService, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
