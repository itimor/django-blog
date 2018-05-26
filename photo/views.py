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
