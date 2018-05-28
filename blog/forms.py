# -*- coding: utf-8 -*-
# author: itimor

from django import forms
from blog.models import Article


class ArticleAddForm(forms.Form):
    name = forms.CharField(label=u'文章标题', max_length=50, widget=forms.TextInput())
    content = forms.CharField(label=u'内容', min_length=50, widget=forms.Textarea())
    tags = forms.CharField(label=u'标签', max_length=30, widget=forms.TextInput({'placeholder': u'文章标签，以空格进行分割'}))

    def save(self):
        cd = self.cleaned_data
        name = cd['name']
        content = cd['content']
        tags = cd['tags']
        article = Article(
            name=name,
            content=content,
            tags=tags)
        article.save()
