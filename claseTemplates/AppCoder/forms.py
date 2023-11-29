from django import forms

class CourseForm(forms.Form):
    name = forms.CharField()
    camada = forms.IntegerField()

class BusquedaCourseForm(forms.Form):
    name = forms.CharField()


class StudentForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()

class searchStudentForm(forms.Form):
    name = forms.CharField()

class ProfessorForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class SearchProfessorForm(forms.Form):
    name = forms.CharField()