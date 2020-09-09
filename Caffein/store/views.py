from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Store 
# Create your views here.

class StoreList(ListView):
    model = Store
    context_object_name = 'all_store'
    template_name = 'store_list.html'

class StoreDetail(DetailView):
    model = Store
    context_object_name = 'one_store'
    template_name = 'store_detail.html'


def index(request):
    
    return render(request,"store_detail.html")


# class PublisherDetail(DetailView):
    # queryset = Publisher.objects.all()

#     model = Publisher

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context