# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from photo.models import Photo, PhotoGroup


class PhotoAdmin(admin.TabularInline):
    model = Photo
    fields = ('group', 'photo', 'desc', 'view_img')
    readonly_fields = ('view_img',)
    exclude = ('view_img',)


class PhotoGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'create_time', 'update_time', 'active')
    list_filter = ('active', 'create_time', 'update_time')
    fields = ('name', 'cover', 'desc', 'active',)
    inlines = [PhotoAdmin, ]


admin.site.register(PhotoGroup, PhotoGroupAdmin)
# admin.site.register(Photo, PhotoAdmin)
