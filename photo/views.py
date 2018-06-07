# -*- coding: utf-8 -*-
# author: itimor

import os
import datetime
import json

from django.views.generic import ListView, View
from photo.models import Photo, PhotoGroup
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import HttpResponse


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


class UploadView(View):
    """ upload image file """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UploadView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        upload_image = request.FILES.get("image-file", None)
        upload_dir = 'post'
        media_root = settings.MEDIA_ROOT

        # image none check
        if not upload_image:
            return HttpResponse(json.dumps({
                'success': 0,
                'message': "未获取到要上传的图片",
                'url': ""
            }))

        # image format check
        file_name_list = upload_image.name.split('.')
        file_extension = file_name_list.pop(-1)
        file_name = '.'.join(file_name_list)

        # image floder check
        file_path = os.path.join(media_root, upload_dir)
        if not os.path.exists(file_path):
            try:
                os.makedirs(file_path)
            except Exception as err:
                return HttpResponse(json.dumps({
                    'success': 0,
                    'message': "上传失败：%s" % str(err),
                    'url': ""
                }))

        # save image
        file_full_name = '%s_%s.%s' % (file_name,
                                       '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()),
                                       file_extension)
        with open(os.path.join(file_path, file_full_name), 'wb+') as file:
            for chunk in upload_image.chunks():
                file.write(chunk)

        return HttpResponse(json.dumps({'success': 1,
                                        'message': "上传成功！",
                                        'url': os.path.join(settings.MEDIA_URL, upload_dir, file_full_name)}))
