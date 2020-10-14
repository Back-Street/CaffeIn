from django.shortcuts import render

# Create your views here.

def choice_registration(request):
    context=dict()
    return render(request, 'choice_regi.html', context)


def registration(request):
    context=dict()
    context['type'] = request.GET.get('type')
    return render(request, 'registration.html', context)


def complete_regi(request):
    return render(request,'complete_regi.html')