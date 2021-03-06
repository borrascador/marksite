"""marksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from views import HomeView, BlackView
from gallery import urls
from donate import urls
from music import urls
from video import urls

'''
from book import urls
from word import urls
from video import urls
from fair import urls
'''

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^book$', BlackView.as_view(), name='book'),
    url(r'^word$', BlackView.as_view(), name='word'),
    url(r'^fair$', BlackView.as_view(), name='fair'),
    url(r'^black$', BlackView.as_view(), name='black') ,
    url(r'^gallery-list/', include('gallery.urls')),
    url(r'^donate/', include('donate.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^video/', include('video.urls')),
    url(r'^photologue/', \
        include('photologue.urls', \
        namespace='photologue')
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
