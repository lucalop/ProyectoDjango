from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Trekking(models.Model):
    title = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    difficulty = models.CharField(max_length=10,null=True)
    duration = models.CharField(max_length=10,null=True)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=40)
    avatar_trekking = models.ImageField(upload_to="Trekking")
    
    date = models.DateField(default=timezone.now)

class Comments(models.Model):
    trekking = models.ForeignKey(Trekking, on_delete=models.CASCADE, related_name="comments") #para crear la relación y que si eliminamos el blog, también los comentarios
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    creation_date = models.DateField(default=timezone.now)

