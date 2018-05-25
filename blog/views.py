# -*- coding: utf-8 -*-
# author: itimor

from django.core.exceptions import PermissionDenied
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Article, Tag, Friend
from utils.pagination import get_pagination
import markdown


class IndexView(ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    # 分页limit
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见get_pagination()。
        pagination_data = get_pagination(paginator, page, is_paginated)

        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)
        return context


class BlogDetailView(DetailView):
    """
    文章详情
    """
    template_name = "detail.html"
    context_object_name = "post"
    queryset = Article.objects.filter(published=True)

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(BlogDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        context = super(BlogDetailView, self).get_object(queryset)

        if not context.published:
            raise PermissionDenied

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        context.body = md.convert(context.body)
        context.toc = md.toc
        return context

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")

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
    context_object_name = "archive_posts"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        return context


class TagView(ListView):
    """
    首页
    """
    template_name = 'tag.html'
    context_object_name = "tag_posts"
    queryset = Article.objects.filter(published=True)

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        context = super(TagView, self).get_queryset().filter(tags__name=tag)
        tags = Tag.objects.all()
        return {'tags': tags, 'tag': tag, 'posts': context}


class PhotoView(ListView):
    """
    首页
    """
    template_name = 'photo.html'
    context_object_name = "photos"
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
    queryset = Friend.objects.filter(active=True)

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
