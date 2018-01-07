# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = "video-list.html"
