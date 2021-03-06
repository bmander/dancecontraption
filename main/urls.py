from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    (r'^$', 'index'),
    url(r'^dance/add/$', 'dance_add'),
    url(r'^dance/(?P<id>\d+)/$', 'dance', name='dance'),
    url(r'^dance/(?P<id>\d+)/event/add/$', 'event_add'),
    url(r'^event/(?P<id>\d+)/attend/$', 'event_attend'),
    url(r'^event/(?P<id>\d+)/unattend/$', 'event_unattend'),
    url(r'^band/(?P<id>\d+)/$', 'band' ),
    url(r'^band/add/$', 'band_add'),
    url(r'^band/search/json/$', 'band_search_json'),
    url(r'^accounts/profile/(\d+)/$', 'profile'),
    url(r'^accounts/profile/$', 'home_profile' ),
    url(r'^accounts/profile/edit/$', 'profile_edit' ),
    url(r'^accounts/signup/$', 'signup', name="signup" ),
    url(r'^accounts/admin/sethome/$', 'set_home_dance',),
    url(r'^accounts/admin/unsethome/$', 'unset_home_dance'),
    url(r'^facebook_auth/$', 'facebook_auth'),
    url(r'^facebook/disconnect/$', 'facebook_disconnect'),
    url(r'^facebook/pull/$', 'facebook_pull'),

    url(r'^person/add/$', 'person_add'),
    url(r'^person/search/json/$', 'person_search_json'),

    url(r'^data/fixattendships/$', 'fixattendships'),
    url(r'^data/fixpeople/$', 'fixpeople'),
    url(r'^data/fixbands/$', 'fixbands'),
)
