"""
URL configuration for claseTemplates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import create_course, show_html, show_courses, create_course_form, busqueda_courses, show_students,create_student_form, create_student, search_student, show_professors, create_professor,create_professor_form, search_professor, CourseList, CourseDetail, CreateCourse, UpdateCourse, DeleteCourse, CreateTrekking , TrekkingDetail  , TrekkingList, search_trekking, AboutMe, comment

urlpatterns = [
    path('agregar_course/', create_course),
    path('course/', create_course_form), #para agregar courses desde el form
    path('buscar/', busqueda_courses),
    path('show/', show_html),
    path('courses/',show_courses),
    path('show/list/', CourseList.as_view(), name="CourseList"),
    path('show/<int:pk>', CourseDetail.as_view(), name="CourseDetail"),
    path('create/', CreateCourse.as_view(), name="CreateCourse"),
    path('edit/<int:pk>', UpdateCourse.as_view(), name="CourseUpdate"),
    path('delete/<int:pk>', DeleteCourse.as_view(), name="CourseDelete"),
    path('showStudents/', show_students),
    path('createStudent/',create_student_form),
    path('createStudent1/',create_student),
    path('searchStudent/',search_student),
    path('showProfessors/', show_professors),
    path('createProfessor/',create_professor_form),
    path('createProfessor/',create_professor),
    path('searchProfessor/',search_professor),
    

    path('trekking/list/', TrekkingList.as_view(), name="TrekkingList"),
    path('create_trekking/', CreateTrekking.as_view(), name="CreateTrekking"),
    path('trekking/<int:pk>', TrekkingDetail.as_view(), name="TrekkingDetail"),
    path('trekking/<int:pk>/comment', comment, name="TrekkingComment"),
    path('search_trekking/', search_trekking, name="SearchTrekking"),
    path('about_me/', AboutMe.as_view(), name="AboutMe")


]














