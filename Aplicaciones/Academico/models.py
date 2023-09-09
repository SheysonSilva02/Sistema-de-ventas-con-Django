from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.dni, self.nombre, self.apellido, self.telefono)

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, default='ValorPredeterminado')
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    ruc = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    

from django.db import models
from .models import Cliente, Producto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)  # Cambia 1 por el ID del producto predeterminado
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)  # Asegúrate de importar timezone correctamente
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.cliente, self.producto, self.cantidad, self.fecha)