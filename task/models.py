from decimal import Decimal
from django.db import models

# Create your models here.
class Task(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2,max_digits=5)
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=100)
    descripcion_categoria = models.CharField(max_length=200)
