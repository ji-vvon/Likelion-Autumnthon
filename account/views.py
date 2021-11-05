from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignupForm
from django.contrib.auth.forms import UserChangeForm

def home(request):
    return render(request, 'home.html')# <임시> 이후 삭제 필요

# Create your views here.
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=auth.authenticate(
                request=request,
                username=username,
                password=password,
            )

            if user is not None:
                auth.login(request,user)
                return redirect('main')# <임시> 이후 메인으로 수정 필요
        return redirect('account:login')
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    auth.logout(request)
    return redirect('main')# <임시> 이후 메인으로 수정 필요

def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth.login(request, user)

            user=UserChangeForm(instance = request.user).save(commit=False)
            user.coin=3
            user.save()
            return redirect('main')
        
        return redirect('account:signup')

    else:
        form=SignupForm()
        return render(request, 'signup.html', {'form':form})