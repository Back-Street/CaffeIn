from django.contrib import admin
from .models import Store,Menu,Review,StorePic,Tag
# Register your models here.

admin.site.register(Store)


admin.site.register(Menu)

admin.site.register(Review)

admin.site.register(StorePic)

admin.site.register(Tag)