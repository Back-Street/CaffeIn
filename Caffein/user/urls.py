from django.urls import path
from .views import choice_registration,registration,complete_regi,login,mypage
urlpatterns=[
    path('choice_registration/',choice_registration, name='choice_registration'),
    path('registration/',registration, name="regi"),
    path('complete_regi/',complete_regi, name="complete_regi"),
    path('login/',login,name="login"),
    path('mypage',mypage,name="mypage")

]