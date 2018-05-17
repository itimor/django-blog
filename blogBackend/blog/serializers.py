# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers

from blog.models import Article, Tag, Friend


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='title')

    class Meta:
        model = Article
        fields = ['url', 'id', 'name', 'slug', 'type', 'content', 'published', 'access_count',
                  'publish_time', 'create_time', 'tags']
        read_only_fields = ('publish_time',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'id', 'name']


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ['url', 'id', 'name', 'link', 'position', 'active']
