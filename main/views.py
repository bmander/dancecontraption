from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from main.models import Dance
from main.forms import DanceForm

def index(request):
    dances = Dance.objects.all() 

    return render_to_response('main/index.html', {'dances':dances})

def dance(request, id):
    dance = Dance.objects.get(pk=id)

    return render_to_response('main/dance.html', {'dance':dance})

def dance_add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = DanceForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    name = form.cleaned_data['name']
	    dance = Dance(name=name)
	    dance.save()
	return HttpResponseRedirect('/') # Redirect after POST

    return render_to_response('main/dance_add.html', {})
