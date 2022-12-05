from django.db import models

# Create your models here.

class Proyecto(models.Model):
  tipo = models.CharField(max_length=50)
  marca = models.CharField(max_length=50)
  modelo = models.CharField(max_length=50)
  capacidad = models.CharField(max_length=50)
  peso = models.CharField(max_length=50)
  garantia = models.CharField(max_length=50)