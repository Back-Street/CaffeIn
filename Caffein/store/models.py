from django.db import models
from django.conf import settings

# Create your models here.
#카페 스토리, 컨텐츠 요소 #카페 인스타 스토리, 카페 아이콘
#전화번호 #위치 # 약도 #운영시간 #특징(단체석, 와이파이) #SNS #메뉴 #리뷰 #사진


class Store(models.Model):
    # host = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    x = models.FloatField('경도')
    y = models.FloatField('위도')
    image = models.ImageField('대표이미지',blank=True)
    like_count = models.PositiveIntegerField(default=0)

    name = models.CharField('이름',max_length=200)
    address = models.TextField('주소',blank=True)
    phone_number = models.CharField('전화번호', max_length=20,blank=True)
    sns = models.TextField('SNS',blank=True)
    open_time = models.TextField("운영시간",blank=True)

    Info = models.TextField("카페이야기",blank=True)
    story = models.FileField("스토리",upload_to="store/story",blank=True)
    icon = models.ImageField("아이콘",upload_to="store/icon",blank=True)
    more_info = models.TextField("세부정보",blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '카페'

    def __str__(self):
        return self.name
class Menu(models.Model):
    class Meta:
        verbose_name_plural = '메뉴'

    store = models.ForeignKey(Store,on_delete=models.SET_NULL, null=True)
    store_menu = models.TextField("가게메뉴",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_menu

class Review(models.Model):
    class Meta:
        verbose_name_plural = '리뷰'

    store = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    user_review = models.TextField("리뷰",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StorePic(models.Model):
    class Meta:
        verbose_name_plural = '사진'
    store = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    class Meta:
        verbose_name_plural = '태그들'
    #나중에 manyto many로 연결해주자
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    pass
