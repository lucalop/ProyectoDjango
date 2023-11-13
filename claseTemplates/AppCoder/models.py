from django.db import models

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    

# Create your models here.
