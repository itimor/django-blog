# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from blog.models import Article, Tag, Friend
from blog.serializers import ArticleSerializer, TagSerializer, FriendSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    ordering_fields = ['publish_time', 'access_count']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
