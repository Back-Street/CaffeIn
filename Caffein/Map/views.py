from django.shortcuts import render
from store.models import Store

# Create your views here.
def map_view(request):
    context = {}
    cafe_list = Store.objects.all()
    context['cafe_list'] = cafe_list
    return render(request, 'map.html', context)