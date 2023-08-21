from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']#model이 사용하는 모든 field
        # fields = ['first_name','last_name','userid','password1','password2','hintPW','nickname','email','signup_date']