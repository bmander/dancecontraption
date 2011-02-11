from django.conf.urls.defaults import *
from django.contrib.auth.views import login

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^login/$', login ),
    (r'^', include('main.urls')),
)
