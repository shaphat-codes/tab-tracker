from django.db import models
from datetime import datetime

# Create your models here.


class NewTab(models.Model):
    url = models.CharField(max_length=1000)
    time_opened = models.CharField(max_length=1000,default=datetime.now, blank=True)
    time_closed = models.CharField(blank=True, default="", max_length=1000)
    diff = models.CharField(blank=True, default="", max_length=1000)


class SwitchTab(models.Model):
    url = models.CharField(max_length=1000)
    time_opened = models.DateTimeField(auto_now_add=True)
    time_closed = models.CharField(blank=True, default="", max_length=1000)
    diff = models.CharField(blank=True, default="", max_length=1000)



