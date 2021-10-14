from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True) #auto_now_add -- 모델이 생설될 때 시간과 날짜를 구함
    updated = models.DateTimeField(auto_now=True) #auto_now_add -- 모델이 업데이트될 때 시간과 날짜를 구함

    class Meta:
        abstract = True
