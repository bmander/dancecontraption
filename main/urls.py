from django.conf.urls.defaults import *

from main.views import dance

urlpatterns = patterns('main.views',
    (r'^$', 'index'),
    url(r'dance/(?P<id>\d+)/$', dance, name='dance')
)
