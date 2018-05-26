# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from blog.storage import PathAndRename


class PhotoGroup(models.Model):
    name = models.CharField(u'标题', max_length=150, unique=True)
    cover = models.ImageField(upload_to=PathAndRename("photocover"), verbose_name=u'封面')
    desc = models.TextField(u'描述', )
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    active = models.BooleanField(u'开启', default=True)

    class Meta:
        verbose_name = u'相册'
        verbose_name_plural = u'相册'


class Photo(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u'标题')
    photo = models.ImageField(upload_to=PathAndRename("photo"), verbose_name=u'照片')
    desc = models.TextField(null=True, blank=True, verbose_name=u'描述')
    group = models.ForeignKey('PhotoGroup', on_delete=models.CASCADE, blank=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name = u'照片'
        verbose_name_plural = u'照片'
