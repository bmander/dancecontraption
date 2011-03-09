from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    (r'^$', 'index'),
    url(r'^dance/add/$', 'dance_add'),
    url(r'^dance/(?P<id>\d+)/$', 'dance', name='dance'),
    url(r'^band/(?P<id>\d+)/$', 'band' ),
    url(r'^accounts/profile/$', 'profile' ),
    url(r'^accounts/signup/$', 'signup', name="signup" ),
    url(r'^accounts/admin/sethome/$', 'set_home_dance',),
    url(r'^accounts/admin/unsethome/$', 'unset_home_dance'),
    url(r'^facebook_auth/$', 'facebook_auth'),
    url(r'^facebook/disconnect/$', 'facebook_disconnect'),
    url(r'^facebook/pull/$', 'facebook_pull'),
)
