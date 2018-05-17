# -*- coding: utf-8 -*-
# author: kiven

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from blog.views import ArticleViewSet, TagViewSet, FriendViewSet

router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagViewSet)
router.register(r'friends', FriendViewSet)

from tool.views import UploadViewSet, FileUploadViewSet

router.register(r'upload', UploadViewSet)
router.register(r'fileupload', FileUploadViewSet)
