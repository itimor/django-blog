# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url
from blog.views import IndexView, BlogDetailView, ArchiveView, TagView, LinkView, GustView, SearchView
from blog.views import ArticleAddView
from blog.views import bad_request, permission_denied, page_not_found, permission_denied

# 定义错误跳转页面
handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = bad_request

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r"^post/view/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="detail"),
    url(r"^post/add", ArticleAddView.as_view(), name="add"),
    url(r"^post/edit/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="edit"),
    url(r'^archive/', ArchiveView.as_view(), name="archive"),
    url(r'^tag/(?P<tag>\w+)', TagView.as_view(), name="tag"),
    url(r'^link', LinkView.as_view(), name="link"),
    url(r'^gust', GustView.as_view(), name="gust"),
    url(r'^search', SearchView.as_view(), name="search"),
]
