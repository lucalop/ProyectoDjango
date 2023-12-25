from django import forms
from AppCoder.models import Trekking , Comments


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

class searchTrekkingTitleForm(forms.Form):
    title = forms.CharField()

class UpdateTrekkingImage(forms.ModelForm):

    class Meta:
        model = Trekking
        #fields = "__all__"
        fields = ("avatar_trekking",)    