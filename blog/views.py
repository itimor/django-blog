# -*- coding: utf-8 -*-
# author: itimor

from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, FormView
from django.http import JsonResponse
from blog.models import Article, Friend, Social
from utils.pagination import get_pagination
import markdown
import operator
from django.db.models import Q
from functools import reduce
from blog.forms import ArticleAddForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import login_required
from taggit.models import Tag


# 自定义错误页面
def bad_request(request):
    data = {"code": 400, "msg": "发生了一个未知的错误"}
    return render(request, 'error.html', data)


def permission_denied(request):
    data = {"code": 403, "msg": "这不是你该来的地方"}
    return render(request, 'error.html', data)


def page_not_found(request):
    data = {"code": 404, "msg": "你进了一个未知的地方"}
    return render(request, 'error.html', data)


def server_error(request):
    data = {"code": 500, "msg": "代码出bug了"}
    return render(request, 'error.html', data)


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            context['social_list'] = Social.objects.all().order_by("-position")[0:4]
        except Exception as e:
            print(e)
        return context


class IndexView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = "posts"
    queryset = Article.objects.filter(published=True)

    # 分页limit
    paginate_by = 10

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


class BlogDetailView(BaseMixin, DetailView):
    """
    文章详情
    """
    template_name = "detail.html"
    context_object_name = "post"
    queryset = Article.objects.filter(published=True)

    def get_object(self, queryset=None):
        context = super(BlogDetailView, self).get_object()

        if not context.published:
            raise PermissionDenied

        # 阅读数增1
        context.views += 1
        context.save(modified=False)

        import re
        re.sub(r'--more--', '', context.content)

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        context.content = md.convert(context.content)

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


class TagView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'tag.html'
    context_object_name = "tag_posts"
    queryset = Article.objects.filter(published=True)

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        json_tags = []

        if tag:
            context = super(TagView, self).get_queryset().filter(tags__slug=tag)
            return {'tag': tag, 'posts': context, 'json_tags': json_tags}
        else:
            from django.db.models import Count
            context = Tag.objects.all()
            queryset = context.annotate(num_times=Count('taggit_taggeditem_items'))
            for tag in queryset:
                json_tags.append({"name": tag.name, "slug": tag.slug, "count": tag.num_times})
            return {'json_tags': json_tags}


class ArchiveView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'archive.html'
    context_object_name = "archive_posts"
    queryset = Article.objects.filter(published=True).order_by("-publish_time")

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        return context


class LinkView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'link.html'
    context_object_name = "posts"
    queryset = Friend.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(LinkView, self).get_context_data(**kwargs)
        return context


class SearchView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'search.html'
    context_object_name = "search_posts"
    queryset = Article.objects.filter(published=True)
    paginate_by = 10

    def get_queryset(self):
        context = super(SearchView, self).get_queryset()

        q = self.request.GET.get('search', '')
        if q:
            query_list = q.split()
            result = context.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result


# 登录用户验证
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# 管理员用户验证
class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AdminRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class ArticleAddView(BaseMixin, LoginRequiredMixin, FormView):
    template_name = 'article_add.html'
    form_class = ArticleAddForm
    success_url = '/'

    @csrf_exempt
    def form_valid(self, form):
        form.save()
        return super(ArticleAddView, self).form_valid(form)
