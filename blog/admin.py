# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from blog.models import Article, Tag, Friend


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
    )

    exclude = ('publish_time',)
    search_fields = ('name', 'published')
    ordering = ('-create_time', 'published', 'publish_time')
    list_per_page = 20


class TagAdmin(admin.ModelAdmin):
    pass


class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'position', 'active')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Friend, FriendAdmin)
