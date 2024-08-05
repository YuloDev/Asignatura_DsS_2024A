from django.db import models
from django.contrib.auth.models import AbstractUser

# Crear el modelo de usuario personalizado
class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# Modelo de categoría
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    record_ventas = models.IntegerField()

    def __str__(self):
        return self.nombre

# Modelo de producto asociado a usuarios de tipo vendedor
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, default="")
    vendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='productos', limit_choices_to={'is_seller': True})
    precio = models.FloatField()
    costo = models.FloatField()

    def __str__(self):
        return self.nombre
