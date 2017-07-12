# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from photologue.models import Gallery



class GalleryView(ListView):
	model = Gallery
	template_name = "gallery.html"
	
