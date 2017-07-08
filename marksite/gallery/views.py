# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):

    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        return context

class ImageView(TemplateView):

    template_name = "images.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        return context
