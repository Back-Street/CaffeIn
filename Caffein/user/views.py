from django.shortcuts import render

# Create your views here.

def choice_registration(request):
    context=dict()
    return render(request, 'choice_regi.html', context)