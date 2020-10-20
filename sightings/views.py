from django.shortcuts import render, get_object_or_404, HttpResponse

from .forms import Form, CreateForm
from .models import Squirrel


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'sightings/index.html', context)


def detail(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Squirrel_ID=squirrel_id)
    if request.method == 'GET':
        # Query detail of the squirrel
        form = Form(instance=squirrel)
        context = {
            'form': form,
            'squirrel_id': squirrel_id
        }
        return render(request, 'sightings/edit.html', context)
    if request.method == 'POST':
        # Edit detail of the squirrel
        form = Form(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'squirrel_id': squirrel_id,
                'success': True
            }
            return render(request, 'sightings/edit.html', context)
        else:
            return HttpResponse('Form data is invalid, invalid fields: ' + form.errors)
    return HttpResponse('Method not supported.')


def show_map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings
    }
    return render(request, 'sightings/map.html', context)


def add(request):
    if request.method == 'GET':
        # Return form
        form = CreateForm()
        context = {
            'form': form
        }
        return render(request, 'sightings/add.html', context)
    if request.method == 'POST':
        # Save the data of the new squirrel
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'success': True
            }
            return render(request, 'sightings/add.html', context)
        else:
            return HttpResponse('Form data is invalid, invalid fields: ' + form.errors)
    return HttpResponse('Method not supported.')


def stats(request):
    # Get stats of all squirrels
    if request.method == 'GET':
        context = {
            'squirrels': Squirrel.objects.all()
        }
        return render(request, 'sightings/stats.html', context)
    else:
        return HttpResponse('Method not supported.')
