from django.shortcuts import render
from .models import Cafe

# Create your views here.
def map_view(request):
    context = {}
    cafe_list = Cafe.objects.all()

    context['cafe_list'] = cafe_list
    return render(request, 'map.html', context)