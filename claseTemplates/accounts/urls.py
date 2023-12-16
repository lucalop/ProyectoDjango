from django.contrib import admin
from django.urls import path, include
from accounts.views import login_request, register_request, edit_request, edit_avatar, MyAccount
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name = "logout"),
    path('register/', register_request, name = "createAccount"),
    path('edit/',edit_request, name="EditUser"),
    path('avatar/',edit_avatar, name ="EditAvatar"),
    path('my_account/<int:pk>/', MyAccount.as_view(), name="MyAccount")

    
]