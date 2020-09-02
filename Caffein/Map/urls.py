from django.urls import path,re_path
from Map.views import Map_view

app_name:'Map'
urlpatterns=[
    path('',Map_view, name='Map'),
]