from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
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
            return redirect('Home')

        return render(request, 'Account/register.html', {'register_form': register_form})

