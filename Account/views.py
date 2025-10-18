from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        register_form = RegisterForm()
        return render(request, 'Account/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            gmail = register_form.cleaned_data.get('gmail')
            password = register_form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, password=password, gmail=gmail)
            user.save()

            messages.success(request, 'با موفقیت ثبت نام شدید')
            return redirect('login')

        return render(request, 'Account/register.html', {'register_form': register_form})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        login_form = LoginForm()
        return render(request, 'Account/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            uoe = login_form.cleaned_data.get('username_or_email')
            password = login_form.cleaned_data.get('password')


            if '@' in uoe:
                user: User = User.objects.filter(gmail=uoe).first()
            else:
                user: User = User.objects.filter(username=uoe).first()

            if user is None or not user.check_password(password):
                messages.error(request, 'نام کاربری/ایمیل یا پسورد وارد شده اشتباه است')

            else:
                login(request, user)
                messages.success(request, 'باموفقیت وارد شدید')
                return redirect('home')

        return render(request, 'Account/login.html', {'login_form': login_form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')








