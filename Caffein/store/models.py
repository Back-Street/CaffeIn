from django.db import models
from django.conf import settings

# Create your models here.
#카페 스토리, 컨텐츠 요소 #카페 인스타 스토리, 카페 아이콘
#전화번호 #위치 # 약도 #운영시간 #특징(단체석, 와이파이) #SNS #메뉴 #리뷰 #사진


class Store(models.Model):
    # host = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address = models.TextField('주소',blank=True)
    phone_number = models.CharField('전화번호', max_length=20,blank=True)
    sns = models.TextField('SNS',blank=True)
    open_time = models.TextField("운영시간",blank=True)

    Info = models.TextField("카페이야기",blank=True)
    story = models.FileField("스토리",upload_to="store/story",blank=True)
    icon = models.ImageField("아이콘",upload_to="store/icon",blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    store = models.ForeignKey(Store,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    store = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StorePic(models.Model):
    store = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    #나중에 manyto many로 연결해주자
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    pass
