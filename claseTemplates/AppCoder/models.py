from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField(unique=False)

    def __str__(self):
        return f"Course: {self.name}, Camada: {self.camada}"


class Students(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
        #Se agregar para que se muestre bien en el admin
    def __str__(self):
        return self.name

class Profesor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    #Se agregar para que se muestre bien en el admin
    def __str__(self):
        return f"Profesor: {self.name} {self.surname}"


class Entregable(models.Model):
    name = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()