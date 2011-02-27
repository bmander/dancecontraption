from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from google.appengine.api import users

from main.models import Dance, Band, Event
from main.forms import DanceForm

def index(request):

    if request.user.is_authenticated():
      login_url = users.create_login_url(dest_url="/")
      logout_url = None
    else:
      login_url = None
      logout_url = users.create_logout_url("/")

    dances = Dance.objects.all() 

    return render_to_response('main/index.html', RequestContext(request, 
                                                 {'dances':dances,
                                                  'login_url':login_url,
						  'logout_url':logout_url}))

@login_required
def profile(request):
    return render_to_response('main/profile.html', RequestContext(request))

def dance(request, id):
    dance = Dance.objects.get(pk=id)

    events = dance.event_set.all().order_by('date')

    return render_to_response('main/dance.html', {'dance':dance, 'events':events})

def band(request,id):
    band = Band.objects.get(pk=id)

    events = band.event_set.all().order_by('date')
    members = band.members.all()

    return render_to_response('main/band.html', {'band':band, 'events':events, 'members':members})

def dance_add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = DanceForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    name = form.cleaned_data['name']
	    dance = Dance(name=name)
	    dance.save()
	return HttpResponseRedirect('/') # Redirect after POST

    return render_to_response('main/dance_add.html', {})

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

            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UserCreationForm()

    return render_to_response('main/signup.html', {
        'form': form,
    })
