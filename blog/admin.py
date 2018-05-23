# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from blog.models import Article, Tag, Friend
import os
from django.dispatch import receiver
from django.db import models


# 图片自动删除
@receiver(models.signals.post_delete, sender=Article)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Photo` object is deleted.
    """
    if instance.cover:
        if os.path.isfile(instance.cover.path):
            os.remove(instance.cover.path)


# 图片自动更新
@receiver(models.signals.pre_save, sender=Article)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Photo` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).cover
    except sender.DoesNotExist:
        return False

    new_file = instance.cover
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type', 'published', 'create_time', 'publish_time', 'views')
    list_filter = ('published', 'publish_time', 'views')
    fields = (
        'name',
        'cover',
        'content',
        'type',
        'published',
        'tags',
        'img_view'
    )

    exclude = ('publish_time',)
    search_fields = ('name', 'published')
    ordering = ('-create_time', 'published', 'publish_time')
    readonly_fields = ('img_view',)
    list_per_page = 20


class TagAdmin(admin.ModelAdmin):
    pass


class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'position', 'active')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Friend, FriendAdmin)
