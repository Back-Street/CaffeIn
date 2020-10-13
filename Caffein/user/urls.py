from django.urls import path
from .views import choice_registration
urlpatterns=[
    path('choice_registration/',choice_registration, name='choice_registration'),
]