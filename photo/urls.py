# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url
from photo.views import PhotoGroupView

app_name = 'photo'
urlpatterns = [
    url(r'', PhotoGroupView.as_view(), name="photogroup"),
]
