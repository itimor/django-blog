# -*- coding: utf-8 -*-
# author: itimor

from django.core.exceptions import PermissionDenied
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from photo.models import Photo, PhotoGroup
from django.db.models import Q


class PhotoGroupView(ListView):
    """
    首页
    """
    template_name = 'photo.html'
    context_object_name = "photos"
    queryset = PhotoGroup.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(PhotoGroupView, self).get_context_data(**kwargs)
        return context
