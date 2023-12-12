from django import forms
from AppCoder.models import Trekking , Comments

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

#Desde acá lo nuevo

class TrekkingForm(forms.ModelForm):

    class Meta:
        model = Trekking
        fields = "__all__"

class TrekkingComment(forms.Form):
    model = Comments
    fields = ("usuario", "trekking", "content")

class searchTrekkingForm(forms.Form):
    city = forms.CharField()