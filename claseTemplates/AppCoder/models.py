from django.db import models
import datetime
from django.contrib.auth.models import User

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

#Esto es lo nuevo

class Trekking(models.Model):
    title = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=40)
    avatar_trekking = models.ImageField(upload_to="Trekking")
    date = models.DateField(default=datetime.datetime.now())

class Comments(models.Model):
    trekking = models.ForeignKey(Trekking, on_delete=models.CASCADE) #para crear la relación y que si eliminamos el blog, también los comentarios
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    creation_date = models.IntegerField(max_length=40)


#class Comments(Blog, Profesor):
#        
#    def __init__(self,title:str ,name:str, surname:str,comment: str ) -> None:
#        self.title = title
#        self.name = name
#        self.surname = surname
#        self.comment = comment

