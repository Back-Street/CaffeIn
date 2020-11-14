from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def choice_registration(request):
    if request.method == 'POST':
        regiform = UserCreationForm(request.POST)
        if regiform.is_valid():
            regiform.save()
            return redirect('choice_regi')
        else:
            return redirect('choice_regi')
    registerform = UserCreationForm
    return render(request, 'choice_regi.html', {'registerform' : registerform})
# registration.html에 form이 있어야함 ~~!

def registration(request):
    context=dict()
    context['type'] = request.GET.get('type')
    return render(request, 'registration.html', context)


def complete_regi(request):
    return render(request,'complete_regi.html')

def caffein_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,
        password=password)

        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            context['message'] = '존재하지 않는 아이디/비밀번호입니다'
            
            return render(request, 'login.html', context)
    else:

        return render(request,'login.html')

def mypage(request):
    return render(request, 'mypage.html')
