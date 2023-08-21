from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# =========================== login / logout ===========================
def sign_in(request):
    if request.method=='GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form' : form})
    
    elif request.method=='POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('posts')
            else:
                messages.error(request,"Invalid username or password")
                return render(request, 'users/login.html',{'form' : form})
                
def sign_out(request):
    logout(request)
    messages.success(request, f"You've been logged out")     
    return redirect('posts')       


# =========================== 회원등록 ===========================
def sign_up(request,false=None):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'users/register.html',{'form':form})
    elif request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=false)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"You've signed up successfully")
            login(request,user) #signup에 성공하면 그것을 이용해서 바로 로그인
            return redirect('posts')
        else : 
            return render(request,'users/register.html',{'form':form})
        
#=========================== 계정 찾기 ===========================
def find_me(request):
    pass