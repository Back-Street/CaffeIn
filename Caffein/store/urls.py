from django.urls import path
from .views import index,StoreList,StoreDetail
urlpatterns=[
    path('detail/<int:pk>',StoreDetail.as_view(), name='store_detail'),
    path("list/",StoreList.as_view(), name="store_list"),
]