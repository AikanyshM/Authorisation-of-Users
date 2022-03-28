from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views

def welcome(request):
    return HttpResponse('Welcome to our company')

def auth_user(request):
    user = request.user
    print(user)

    return HttpResponse(user.username)


def check_user(request):
    if request.method == "GET":
        return render(request, 'create_user.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username, password = password)
        user.save()

        return HttpResponse(f'Пользователь {user.username} создан')

def change_password(request):
    if request.method == "GET":
        return render(request, 'create_user.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return HttpResponse(f'У пользователя {user.username} пароль изменен')

def login_view(request):
    if request.method == "GET":
        return render(request, 'create_user.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if request.user.is_authenticated:
            return render(request, 'auth.html')
        else:
            return HttpResponse("Попробуйте еще раз!")

def logout_view(request):
    logout(request)
    return HttpResponse("До свидания")



    