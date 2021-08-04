from django.db import models


class Post(models.Model):
    message = models.TextField(verbose_name="메세지")
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
