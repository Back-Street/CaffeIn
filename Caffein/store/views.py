from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from .models import Store,Menu 
from user.models import CaffeInUser
from django.shortcuts import render, redirect,HttpResponseRedirect
# Create your views here.

class StoreList(ListView):
    model = Store
    context_object_name = 'all_store'
    template_name = 'store_list.html'

class StoreDetail(DetailView):
    model = Store
    context_object_name = 'one_store'
    template_name = 'store_detail.html'


@login_required(login_url='login')
def like_toggle(request, store_id):
    user = request.user
    store = Store.objects.get(id=store_id)

    try:
        check = user.likes.all().get(id=store_id)
        user.likes.remove(store_id)
        store.like_count -= 1
        store.save()
    except:
        user.likes.add(store_id)
        store.like_count += 1
        store.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def index(request):
    
    return render(request,"store_detail.html")

def search(request):
    context=dict()
    store_list = Store.objects.all()
    store = request.POST.get('search',"")

    if store:
        store_list = store_list.filter(name__icontains=store)
        context['store_list'] = store_list
        context['search'] = search
        return render(request,'search.html',context)
    else:
        return render(request,'search.html')


# def search(request):
#     context=dict()
#     store_list = Store.objects.all()
#     store = request.POST.get('search',"")

#     if store:
#         store_list = store_list.filter(name__icontains=store)
#         context['store_list'] = store_list
#         context['search'] = search
#         return render(request,'search.html',context)
#     else:
#         return render(request,'search.html')


# class PublisherDetail(DetailView):
    # queryset = Publisher.objects.all()

#     model = Publisher

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context