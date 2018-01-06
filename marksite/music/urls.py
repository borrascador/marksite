from django.conf.urls import url
from .views import SongListView



urlpatterns = [
    url(r'^$', SongListView.as_view(), name='music'),
]
