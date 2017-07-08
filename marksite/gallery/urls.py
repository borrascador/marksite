from django.conf.urls import url
from gallery.views import HomeView, ImageView

urlpatterns = [
    url(r'$^', HomeView.as_view(), name='home'),
    url(r'^images/', ImageView.as_view(), name='images'),
    #url(r'^drawings/', ),
    #url(r'^songs/', ),
    #url(r'^poems/', ),
    #url(r'^video/', ),
    #url(r'store/', ),
]
