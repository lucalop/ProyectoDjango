from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):
    curso = Curso(nombre = "Pyhton", camada = 47785)
    curso.save()

    return HttpResponse(str(curso.nombre))