from django.urls import path
from .views import index,StoreList,StoreDetail,like_toggle
urlpatterns=[
    path('detail/<int:pk>',StoreDetail.as_view(), name='store_detail'),
    path("list/",StoreList.as_view(), name="store_list"),
    path("like_toggle/<int:store_id>/",like_toggle,name='like_toggle')
]