# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from tool.models import Upload, FileUpload
from tool.serializers import UploadSerializer, FileUploadSerializer


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all().order_by("-create_time")
    serializer_class = UploadSerializer
    filter_fields = ('username', 'type',)


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = (AllowAny,)