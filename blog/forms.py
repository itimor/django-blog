# -*- coding: utf-8 -*-
# author: itimor

from django import forms
from blog.models import Article, BlogTypes
from mdeditor.fields import MDTextFormField


class ArticleAddForm(forms.Form):
    name = forms.CharField(label=u'文章标题', max_length=50)
    cover = forms.ImageField(label=u'封面', )
    content = MDTextFormField(label=u'内容', min_length=50)
    type = forms.ChoiceField(label=u'分类', choices=BlogTypes)
    tags = forms.CharField(label=u'标签', max_length=50)

    def save(self):
        cd = self.cleaned_data
        print(cd)
        name = cd['name']
        cover = cd['cover']
        type = cd['type']
        content = cd['content']
        tags = cd['tags']
        article = Article(
            name=name,
            cover=cover,
            content=content,
            type=type,
            tags=tags)
        article.save()
