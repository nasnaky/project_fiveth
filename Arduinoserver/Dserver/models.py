from django.db import models


class TEMPERATURE(models.Model):  # 온도
    TEMP = models.IntegerField()
    TIME = models.DateTimeField(auto_now_add=True)


class HUMIDITY(models.Model):  # 습도
    DEGREE = models.IntegerField()
    TIME = models.DateTimeField(auto_now_add=True)


class REMNANT_W(models.Model):
    WATER = models.IntegerField()
    TIME = models.DateTimeField(auto_now_add=True)


class CAMERA(models.Model):
    TITLE = models.TextField()
    LINK = models.URLField()
    