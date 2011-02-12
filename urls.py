from django.conf.urls.defaults import *
from django.contrib.auth.views import login

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^login/$', 'main.views.login' ), #try using django.contrib.auth.views.login instead
    (r'^', include('main.urls')),
)
