# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime

import requests
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']

@receiver(post_save, sender=Question)
def renewal(sender, instance, created, **kwargs):
    if created:
        requests.post("http://localhost:8006/create/message", data={"message": instance.id})
