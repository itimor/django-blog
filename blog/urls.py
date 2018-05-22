# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url
from blog.views import IndexView, BlogDetailView, ArchiveView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='blog_list'),
    url(r"^post/(?P<pk>\d+)/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="blog_detail"),
    # url(r'^comment/add/(?P<pk>[0-9]+)$', CommentView.as_view()),
    # url(r'^comment/delete/(?P<pk>[0-9]+)$', CommentDeleteView.as_view()),
    # url(r'^repository$', RepositoryView.as_view()),
    # url(r'^repository/(?P<pk>[0-9]+)$', RepositoryDetailView.as_view()),
    # url(r'^tags/(?P<slug>[\w\u4e00-\u9fa5]+)$', TagListView.as_view()),
    # url(r'^category/(?P<slug>[\w\u4e00-\u9fa5]+)$', CategoryListView.as_view()),
    url(r'^archive/', ArchiveView.as_view())
]