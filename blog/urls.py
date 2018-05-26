# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url
from blog.views import IndexView, BlogDetailView, ArchiveView, TagView, LinkView, GustView, SearchView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r"^post/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="detail"),
    url(r'^archive/', ArchiveView.as_view(), name="archive"),
    url(r'^tag/(?P<tag>\w+)', TagView.as_view(), name="tag"),
    url(r'^link', LinkView.as_view(), name="link"),
    url(r'^gust', GustView.as_view(), name="gust"),
    url(r'^search', SearchView.as_view(), name="search"),
]
