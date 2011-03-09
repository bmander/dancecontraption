from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from google.appengine.api import users

from main.models import Dance, Band, Event, Homeship, UserProfile, FacebookLink
from main.forms import DanceForm, EventForm, BandForm

from secrets import APP_SECRET
from google.appengine.api.urlfetch import fetch

from django.utils import simplejson as json
import settings

def index(request):

    dances = Dance.objects.all() 
    bands = Band.objects.all()

    return render_to_response('main/index.html', RequestContext(request, 
                                                 {'dances':dances,
                                                  'bands':bands}))

def profile(request, id):
    user = User.objects.get(pk=id)
    profile = user.get_profile()

    return render_to_response('main/profile.html', RequestContext(request, {'profile':profile}))

@login_required
def home_profile(request):
    profile = request.user.get_profile()

    return render_to_response('main/home_profile.html', RequestContext(request, {'profile':profile}))

def dance(request, id):
    dance = Dance.objects.get(pk=id)

    events = dance.event_set.all().order_by('date')

    # user's home dance?
    homeship=None
    if request.user and request.user.is_authenticated():
        try:
            homeship = Homeship.objects.get(user=request.user,dance=dance)
	except Homeship.DoesNotExist:
	    pass

    homeships = Homeship.objects.select_related('user').filter(dance=dance)

    return render_to_response('main/dance.html', RequestContext(request,{'dance':dance, 'events':events, 'homeship':homeship, 'homeships':homeships}))

def band(request,id):
    band = Band.objects.get(pk=id)

    events = band.event_set.all().order_by('date')
    members = band.members.all()

    return render_to_response('main/band.html', RequestContext(request, {'band':band, 'events':events, 'members':members} ))

def dance_add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = DanceForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            dance = Dance(name=name)
            dance.save()
            return HttpResponseRedirect('/') # Redirect after POST

    return render_to_response('main/dance_add.html', {})

def event_add(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.instance
            event.save()
            return HttpResponseRedirect( reverse( 'main.views.dance', args=(event.dance.id,) ) )
        
    else:
        form = EventForm()

    return render_to_response('main/event_add.html', {'form':form})

def band_add(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.instance
            band.save()
            return HttpResponseRedirect( "/" )
    else:
        form = BandForm()

    return render_to_response('main/band_add.html', {'form':form})

def signup(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
                        
            user = User.objects.create_user(form.cleaned_data['username'], 
                                            "",
                                            form.cleaned_data['password1'])
            
            user = authenticate(username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password1'])
            
            login( request, user )

            UserProfile(user=user).save()

            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UserCreationForm()

    return render_to_response('main/signup.html', {
        'form': form,
    })

def set_home_dance(request):
    dance = Dance.objects.get(pk=request.GET['dance'])

    homeship = Homeship.objects.get_or_create(user=request.user, dance=dance)

    return HttpResponseRedirect("/dance/%s/"%dance.id)

def unset_home_dance(request):
    dance = Dance.objects.get(pk=request.GET['dance'])

    try:
      homeship = Homeship.objects.get(user=request.user, dance=dance)
      homeship.delete()
    except Homeship.DoesNotExist:
      pass

    return HttpResponseRedirect("/dance/%s/"%dance.id)

def get_facebook_access_token(oauth_code):
    redirect_uri='http://localhost:8000/facebook_auth'

    url = "https://graph.facebook.com/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s"%(settings.FACEBOOK_APP_ID,redirect_uri,APP_SECRET,oauth_code)

    return fetch( url ).content

def get_facebook_profile(access_token):
    url = "https://graph.facebook.com/me?"+access_token 

    return json.loads( fetch( url ).content )

def get_facebook_friends(access_token):
    url = "https://graph.facebook.com/me/friends?"+access_token

    return json.loads( fetch( url ).content )

def facebook_auth(request):
    oauth_code = request.GET['code']

    access_token = get_facebook_access_token(oauth_code)

    facebook_profile = get_facebook_profile( access_token )

    facebook_link = FacebookLink(oauth_code=oauth_code,
                                 access_token=access_token,
                                 account_id = facebook_profile['id'],
                                 name = facebook_profile['name'],
                                 link = facebook_profile['link'])
    facebook_link.save()

    profile = request.user.get_profile()
    profile.facebook = facebook_link
    profile.save()

    return HttpResponseRedirect( "/accounts/profile" )

def facebook_disconnect(request):
    profile = request.user.get_profile()
    profile.facebook = None
    profile.save()

    return HttpResponseRedirect( "/accounts/profile" )

def facebook_pull(request):
    profile = request.user.get_profile()
    
    facebook = profile.facebook

    if facebook is None:
        return HttpResponse("ain't got no facebook")

    return HttpResponse( str(get_facebook_friends(facebook.access_token)) )
