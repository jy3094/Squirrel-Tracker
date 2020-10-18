from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Squirrel


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels
    }
    return render(request, 'sightings/index.html', context)

def detail(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Squirrel_ID=squirrel_id)
   
    context = {
        'squirrel':squirrel,
    }

    return render(request, 'sightings/detail.html', context)
