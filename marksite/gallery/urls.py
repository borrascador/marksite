from django.conf.urls import url
from gallery.views import ImageView

urlpatterns = [
    url(r'images/', ImageView.as_view(), name='images'),
]
