# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

APPEND_SLASH = True
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'', include('blog.urls')),
    url(r'^photo/', include('photo.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'mdeditor/', include('mdeditor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
