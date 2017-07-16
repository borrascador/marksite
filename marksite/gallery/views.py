# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from photologue.models import Gallery, Photo



class GalleryListView(ListView):
	model = Gallery
	template_name = "gallery-list.html"
	
class ImageDetailView(DetailView):
    model = Photo    
    template_name = "image-detail.html"
    
    def gallery(self):
        return Gallery.objects.get(slug = self.kwargs['galleryslug'])
