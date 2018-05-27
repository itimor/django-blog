# -*- coding: utf-8 -*-
# author: itimor

from django.core.exceptions import PermissionDenied
from django.views.generic.list import ListView
from photo.models import Photo, PhotoGroup


class PhotoGroupView(ListView):
    """
    首页
    """
    template_name = 'photogroup.html'
    context_object_name = "photogroups"
    queryset = PhotoGroup.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(PhotoGroupView, self).get_context_data(**kwargs)
        return context


class PhotoView(ListView):
    """
    首页
    """
    template_name = 'photo.html'
    context_object_name = "photos"
    queryset = Photo.objects.all()

    def get_queryset(self):
        group = self.kwargs.get('group')
        context = super(PhotoView, self).get_queryset().filter(group__name=group)
        return context

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)

        group = self.kwargs.get('group')
        group_id = PhotoGroup.objects.get(name=group).id

        prev_post = None
        next_post = None

        try:
            prev_post = PhotoGroup.objects.get(active=True, pk=(group_id - 1))
        except Exception as e:
            print(e)

        try:
            next_post = PhotoGroup.objects.get(active=True, pk=(group_id + 1))
        except Exception as e:
            print(e)

        context['prev_post'] = prev_post
        context['next_post'] = next_post
        return context