# -*- coding: utf-8 -*-
# author: itimor

import os
from django.utils.deconstruct import deconstructible
from re import sub
import time
import random


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, file):
        filename = os.path.splitext(file)
        fntime = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(10, 99)
        last_filename = "%s-%s%s" % (sub('\W+', '', filename[0]), fntime, filename[1])
        return os.path.join(self.path, last_filename)
