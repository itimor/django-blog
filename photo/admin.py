# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from photo.models import Photo, PhotoGroup


class PhotoGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'create_time', 'update_time', 'active')
    list_filter = ('active', 'create_time', 'update_time')
    fields = ('name', 'cover', 'desc', 'active',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'group', 'create_time', 'update_time')
    list_filter = ('group', 'create_time', 'update_time')
    fields = ('name', 'photo', 'desc', 'group')


admin.site.register(PhotoGroup, PhotoGroupAdmin)
admin.site.register(Photo, PhotoAdmin)
