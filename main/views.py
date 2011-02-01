from django.http import HttpResponse
from django.shortcuts import render_to_response

from main.models import Dance

def index(request):
    dances = Dance.objects.all() 

    return render_to_response('main/index.html', {'dances':dances})

def dance(request, id):
    dance = Dance.objects.get(pk=id)

    return render_to_response('main/dance.html', {'dance':dance})
