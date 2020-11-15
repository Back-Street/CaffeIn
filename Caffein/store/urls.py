from django.urls import path
from .views import index,StoreList,StoreDetail,like_toggle,search,StoreUpdate,update_menu
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('detail/<int:pk>',StoreDetail.as_view(), name='store_detail'),
    path('update/<int:pk>',StoreUpdate.as_view(), name='store_update'),
    path('update_menu/<int:store_id>/<int:menu_id>',update_menu,name="update_menu"),
    path("list/",StoreList.as_view(), name="store_list"),
    path("like_toggle/<int:store_id>",like_toggle,name='like_toggle'),
    path('search/',search,name="search"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

