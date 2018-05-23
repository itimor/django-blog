# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url
from blog.views import IndexView, BlogDetailView, ArchiveView, PhotoView, LinkView, GustView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='blog_list'),
    url(r"^post/(?P<pk>\d+)/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="blog_detail"),
    url(r'^archive', ArchiveView.as_view()),
    url(r'^photo', PhotoView.as_view()),
    url(r'^link', LinkView.as_view()),
    url(r'^gust', GustView.as_view()),
]
