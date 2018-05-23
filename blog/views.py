# -*- coding: utf-8 -*-
# author: itimor

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import PermissionDenied
from blog.models import Article, Tag, Friend


class IndexView(ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class BlogDetailView(DetailView):
    """
    文章详情
    """
    template_name = "post.html"
    context_object_name = "post"
    queryset = Article.objects.filter(published=True)

    def get_object(self, queryset=None):
        context = super(BlogDetailView, self).get_object(queryset)

        if not context.published:
            raise PermissionDenied

        # 阅读数增1
        context.access_count += 1
        context.save(modified=False)
        return context

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")

        page = dict()
        page['comments'] = True
        page['title'] = current_post.title
        page['path'] = current_post.get_absolute_url
        context['page'] = page

        prev_post = None
        next_post = None

        try:
            prev_post = Article.objects.get(published=True, pk=(current_post.id - 1))
        except Exception as e:
            print(e)

        try:
            next_post = Article.objects.get(published=True, pk=(current_post.id + 1))
        except Exception as e:
            print(e)

        context['prev_post'] = prev_post
        context['next_post'] = next_post
        return context


class ArchiveView(ListView):
    """
    首页
    """
    template_name = 'archive.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        return context


class PhotoView(ListView):
    """
    首页
    """
    template_name = 'photo.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        return context


class LinkView(ListView):
    """
    首页
    """
    template_name = 'link.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(LinkView, self).get_context_data(**kwargs)
        return context


class GustView(ListView):
    """
    首页
    """
    template_name = 'gust.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(GustView, self).get_context_data(**kwargs)
        return context
