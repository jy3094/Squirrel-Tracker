from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Squirrel
from .forms import Form

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

def edit(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Squirrel_ID=suqirrel_id)
    if request.method=='Post':
        form = Form(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
        else:
            form = Form(instance=squirre)
        context = {
                'form':form
        }
        return render(request,'sightings/edit.html',context)
