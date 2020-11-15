from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CaffeInUserManager, CaffeInUser

# Create your views here.

def choice_registration(request):
    context=dict()
    return render(request, 'choice_regi.html', context)


def registration(request):
    # context=dict()
    if request.method == 'POST':
        # if request.POST['password'] == request.POST['password_confirm']:
        user = CaffeInUser.objects.create_user(user_id=request.POST['user_id'],username=request.POST['username'],confirm_cafe=request.POST['confirm_cafe'],
        user_phone=request.POST['user_phone'],cafeloca=request.POST['cafeloca'],password=request.POST['password'],)
        login(request, user)
        return redirect('login')
    return render(request, 'registration.html')

def complete_regi(request):
    return render(request,'complete_regi.html')

def caffein_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            context['message'] = '존재하지 않는 아이디/비밀번호입니다'
            
            return render(request, 'login.html', context)
    else:

        return render(request,'login.html')

def caffein_logout(request):
    if request.method == 'POST':
        logout(request, user)
        return redirect('/')

    return render(request, 'login.html')

def mypage(request):
    return render(request, 'mypage.html')
