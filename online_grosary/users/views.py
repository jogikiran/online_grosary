from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User


def register_user_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password_one = request.POST['password_one']
        password_two = request.POST['password_two']

        if password_one == password_two:
            if User.objects.filter(username=username).exists():
                messages.warning(request, f"username {username} is already taken, plese give alternative")
                return redirect("/users/register-users/")
            else:
                User.objects.create_user(username=username, password=password_one, )
                messages.success(request, f"user create successfully {username}")
                return redirect("/users/login-users/")
        else:
            messages.warning(request, f"password and conformpassword is not matched")
            return redirect("/users/register-users/")
        
    return render(request, 'users_templates/register_users.html')


def login_user_view(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"login successfully {username}")
            return redirect("/grosary/grosary-list/")
    return render(request, 'users_templates/login_users.html')


def logout_user(request):
    logout(request)
    return redirect("/grosary/grosary-list/")

