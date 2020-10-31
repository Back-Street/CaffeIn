from django.urls import path
from .views import index,StoreList,StoreDetail,search
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('detail/<int:pk>',StoreDetail.as_view(), name='store_detail'),
    path("list/",StoreList.as_view(), name="store_list"),
    path("search/",search, name="search"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)