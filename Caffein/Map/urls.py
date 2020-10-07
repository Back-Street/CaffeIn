from django.urls import path
from Map.views import map_view
from django.conf.urls.static import static
from django.conf import settings

app_name:'Map'
urlpatterns=[
    path('',map_view, name='map'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)