from django.shortcuts import render, redirect
from AppCoder.models import Course, Students, Profesor
from django.http import HttpResponse
from AppCoder.forms import CourseForm,BusquedaCourseForm, searchStudentForm, StudentForm,ProfessorForm, SearchProfessorForm


# Create your views here.

def create_course(request):

    course = Course(name = "Pyhton", camada = 345345)
    course.save()

    return redirect ('/app/courses') #para redireccionar

def create_course_form(request):
    if request.method == "POST":
        # Crear course
        course_formulario = CourseForm(request.POST)
        if course_formulario.is_valid():
            informacion = course_formulario.cleaned_data
            course_crear = Course(name=informacion["name"], camada=informacion["camada"])
            course_crear.save()
            return redirect("/app/courses/")

    course_formulario = CourseForm()
    contexto = {
        "form": course_formulario
    }
    return render(request, "AppCoder/create_course.html", contexto)


def show_html(request):
    course = Course.objects.first()
    contexto = {"course": course, "name": "Lucas"}
    return render(request,'index.html',contexto)

def show_courses(request):
    courses = Course.objects.all()
    contexto = {
        "courses": courses,
        "form": BusquedaCourseForm(),
        }
    
    return render(request,'AppCoder/courses.html',contexto)

def busqueda_courses(request):
    name = request.GET["name"]
    courses= Course.objects.filter(name__icontains=name)
    contexto = {
        "courses": courses,
        "form": BusquedaCourseForm(),
        }
    
    return render(request,'AppCoder/courses.html',contexto)


def show_students(request):
    students = Students.objects.all()
    contexto = {
        "students": students,
        "form": searchStudentForm(),
        }
    return render(request,'AppCoder/students.html',contexto)

def create_student(request):

    student = Students(name = "Lucas22", surname = "lop22", email= "22luclop@maail.com")
    student.save()

    return redirect ('/app/showStudents') #para redireccionar    

def create_student_form(request):
    if request.method == "POST":
        # Crear course
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            informacion = student_form.cleaned_data
            create_student = Students(name=informacion["name"], surname=informacion["surname"], email=informacion["email"])
            print("hasta acá bien)")
            create_student.save()
            return redirect("/app/showStudents/")

    student_form = StudentForm()
    contexto = {
        "form": student_form
    }
    return render(request, "AppCoder/create_student.html", contexto)

def search_student(request):
    name = request.GET["name"]
    students= Students.objects.filter(name__icontains=name)
    contexto = {
        "students": students,
        "form": SearchProfessorForm(),
        }
    
    return render(request,'AppCoder/students.html',contexto)


def show_professors(request):
    professors = Profesor.objects.all()
    contexto = {
        "professors": professors,
        "form": SearchProfessorForm(),
        }
    return render(request,'AppCoder/professors.html',contexto)

def create_professor(request):

    professor = Profesor(name = "Lucas22", surname = "lop22", email= "22luclop@maail.com")
    professor.save()

    return redirect ('/app/showprofessors') #para redireccionar    

def create_professor_form(request):
    if request.method == "POST":
        # Crear course
        professor_form = ProfessorForm(request.POST)
        if professor_form.is_valid():
            informacion = professor_form.cleaned_data
            create_professor = Profesor(name=informacion["name"], surname=informacion["surname"], email=informacion["email"], profesion=informacion["profesion"])
            print("hasta acá bien)")
            create_professor.save()
            return redirect("/app/showProfessors/")

    professor_form = ProfessorForm()
    contexto = {
        "form": professor_form
    }
    return render(request, "AppCoder/create_professor.html", contexto)

def search_professor(request):
    name = request.GET["name"]
    professors= Profesor.objects.filter(name__icontains=name)
    contexto = {
        "professors": professors,
        "form": SearchProfessorForm(),
        }
    
    return render(request,'AppCoder/professors.html',contexto)

def delete_course(request):
    nombre=request.GET["nombre"]
    curso=Course.objects.get(nombre=nombre)
    curso.delete()
    return redirect ("/app/courses")
















"""
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
class CourseList(ListView):
    model = Course
    template_name = "AppCoder/courses1.html"


class CourseDetail(DetailView):
    model = Course
    template_name = "AppCoder/course_detail.html"

class CreateCourse(CreateView):
    model = Course
    success_url = "/app/show/list"
    template_name = "AppCoder/create_course.html"
    fields= ["name","camada"]

class UpdateCourse(UpdateView):
    model = Course
    success_url = "/app/show/list"
    template_name = "AppCoder/create_course.html"
    fields= ["name","camada"]

class DeleteCourse(DeleteView):
    model = Course
    success_url = "/app/show/list"
    template_name = "AppCoder/delete_course.html"
"""