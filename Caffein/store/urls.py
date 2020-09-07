from django.urls import path
from .views import index 
urlpatterns=[
    path('detail/',index, name='store_detail'),
]