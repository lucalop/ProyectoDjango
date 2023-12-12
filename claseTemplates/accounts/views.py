from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('TrekkingList')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form =UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect ("TrekkingList")

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)



@login_required #Lo que hace es que ya trae el usuario cuando haceel request
def edit_request(request):

    user= request.user

    if request.method =="POST":

        form=UserUpdateForm(request.POST)
        if form.is_valid():
            user.email = request.POST["email"]
            user.last_name= request.POST["last_name"]
            user.save()
            return redirect("MyAccount")
    
    form = UserUpdateForm(initial = {"username": user.username, "email":user.email})
            
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)

@login_required #Lo que hace es que ya trae el usuario cuando haceel request
def edit_avatar(request):

    user= request.user
    if request.method =="POST":

        form=AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except: 
                avatar = Avatar(
                    user=user,
                    imagen= data["imagen"]
                )
            

            avatar.save()
            return redirect("MyAccount")
    form = AvatarUpdateForm()
            
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)

class MyAccount(DetailView):
    model = User
    template_name = "accounts/my_account.html"

    
    
