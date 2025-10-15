from django import forms
from .models import *
from django.core.validators import RegexValidator

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
        validators = [RegexValidator(
            r'^[a-zA-Z][a-zA-Z0-9_]{4,}$',
            message='فقط حروف انگلیسی و اعداد مجاز هستند و باید بیشتر از 5 کاراکتر باشد'
        )]
    )

    gmail = forms.CharField(
        max_length=100,
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'})
    )

    password = forms.CharField(
        max_length=100,
        label='پسورد',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'پسورد'})
    )

    confirm_password = forms.CharField(
        max_length=100,
        label='تکرار پسورد',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار پسورد'})
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("پسورد با تکرارش برابر نیست")
        return confirm_password
