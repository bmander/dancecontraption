from django.conf.urls.defaults import *
from django.contrib.auth.views import login

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login' ), #try using django.contrib.auth.views.login instead
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login' ),
    (r'^accounts/profile/$', 'main.views.profile' ),
    (r'^', include('main.urls')),
)
