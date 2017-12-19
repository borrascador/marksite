from django.conf.urls import url
from .views import GalleryListView, ImageDetailView



urlpatterns = [
	url(r'^$', GalleryListView.as_view(), name='gallery-list'),
  url(r'^(?P<galleryslug>[\-\d\w]+)/(?P<slug>[\-\d\w]+)/$', \
    ImageDetailView.as_view(), name='image'),
]
