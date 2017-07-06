from django.conf.urls import url
from gallery.views import HomeView

urlpatterns = [
    url(r'$^', HomeView.as_view(), name='home'),
    #url(r'^photos/', .......),
    #url(r'^drawings/', ),
    #url(r'^songs/', ),
    #url(r'^poems/', ),
    #url(r'^video/', ),
    #url(r'store/', ),
]
