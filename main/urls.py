from django.conf.urls.defaults import *

from main.views import dance, dance_add

urlpatterns = patterns('main.views',
    (r'^$', 'index'),
    url(r'dance/add/$', dance_add),
    url(r'dance/(?P<id>\d+)/$', dance, name='dance'),
    url(r'band/(?P<id>\d+)/$', 'band' )
)
