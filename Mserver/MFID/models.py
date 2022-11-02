from django.db import models


class USER(models.Model):
    NAME = models.TextField()
    PASSWORD = models.TextField()


class SERVER(models.Model):
    LINK = models.URLField()
    TITLE = models.TextField()
    CENTENT = models.TextField()
    STATUS = models.IntegerField(default=0)
    USER = models.ForeignKey(USER, on_delete=models.CASCADE)
