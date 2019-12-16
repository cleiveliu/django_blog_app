from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def register_user(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        new_user = User(username=username)
        new_user.set_password(password)

        new_user.save()
        login(request, new_user)
        messages.info(request, "您已成功注册")

        return redirect("index")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    form = LoginForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "用户名或密码错误")
            return render(request, "login.html", context)

        messages.success(request, "您已成功登录")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "您已成功注销")
    return redirect("index")
