from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField('카페이름', max_length=20)
    x = models.FloatField('경도')
    y = models.FloatField('위도')
    image = models.ImageField('카페사진',blank=True)

    def __str__(self):
        return self.name