# El presente proyecto corresponde a la entrega N°3 del curso de Python|Coderhouse
## Requisitos del proyecto:
 Desarrollar una WEB Django con patrón MVT subida a Github que incluya_
- Herencia de HTML
- Por lo menos 3 clases en models
- Un formulario para insertar a todas las clases de tu modelo
- Un formulario para buscar algo en la BD
- Readme

# Prerequisitos
Instalar Python (Idealmente V3.11)
Instalar Django

# Pasos para clonar el proyecto:
- Dirigirse a la carpeta local en la cual se desea clonar el proyecto
- Abrir terminal y escribir el comando "git clone https://github.com/lucalop/ProyectoDjango.git"


# Pasos para correr el proyecto
Abrir terminal y escribir los siguientes comandos en orden: 
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver     

Para poder hacer uso de la app dirigirse a 

http://127.0.0.1:8000/app/courses/

# Funcionalidades

## Se cuenta con 3 clases: Cursos, Profesores y alumnos. El panel de navegación cuenta con 6 botones:

- Create Course: Solicita nombre y camada para poder crear un curso en la base de datos.
- Coruses: Muestra todos los cursos existentes y posee un buscador para poder filtrar cursos de acuerdo al nombre que se le indique

- Create Professor: Solicita los campos Nombre, Apellido, email y profesión para poder crear un profesor en la base de datos.
- Professors: Muestra todos los profesores existentes y posee un buscador para poder filtrar profesores de acuerdo al nombre que se le indique

- Create Student: Solicita los campos Nombre, Apellido e email para poder crear un estudiante en la base de datos.
- Students: Muestra todos los estudiantes existentes y posee un buscador para poder filtrar estudiantes de acuerdo al nombre que se le indique
