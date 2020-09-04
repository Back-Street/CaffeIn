from django.urls import path,re_path
from Map.views import map_view

app_name:'Map'
urlpatterns=[
    path('',map_view, name='Map'),
]