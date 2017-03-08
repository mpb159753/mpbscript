# encoding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DWT(models.Model):
    show = models.CharField(max_length=50)      # 属于哪个节目（锵锵三人行或圆桌派）
    title = models.CharField(max_length=50)
    page_url = models.URLField()
    video_url = models.URLField(null=True, blank=True)
    date = models.DateField()