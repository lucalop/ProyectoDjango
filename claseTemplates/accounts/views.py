from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar
from django.views.generic import  DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

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
                messages.success(request, '¡Sucessfully login!')
                return redirect('TrekkingList')
            else:
                form.add_error(None, 'Incorrect Username or password')
        else:
            messages.error(request, 'Incorrect Username or password')

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
            messages.success(request, 'Sucessfully signed up! Now you can login')
            return redirect ("TrekkingList")
        else: print("Invalid form:", form.errors)
    else:
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
            messages.success(request, '¡Account information updated!')

            return redirect("TrekkingList")
            
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
    else:
        form = AvatarUpdateForm()
            
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)

class MyAccount(DetailView):
    model = User
    template_name = "accounts/my_account.html"

    
    
