from django.shortcuts import render

# Create your views here.
def Map_view(request):
    return render(request, 'map.html')