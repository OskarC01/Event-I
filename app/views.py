from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Location, Event
from .forms import EventForm, LocationForm


def mainpage(request):
    approved_events = Event.objects.filter(approved=True)
    total_events = approved_events.count()

    context = {'approved_events': approved_events,
               'total_events': total_events}
    return render(request, 'mainpage.html', context)


@login_required(login_url='/login/')
def all_events(request):
    events = Event.objects.all()
    total_events = events.count()

    context = {'events': events, 'total_events': total_events}
    return render(request, 'all_events.html', context)


@login_required(login_url='/login/')
def event(request, pk):
    event = Event.objects.get(id=pk)

    context = {'event': event}
    return render(request, 'event.html', context)


@login_required(login_url='/login/')
def all_locations(request):
    locations = Location.objects.all()
    total_locations = locations.count()

    context = {'locations': locations, 'total_locations': total_locations}
    return render(request, 'all_locations.html', context)


@login_required(login_url='/login/')
def location(request, pk):
    location = Location.objects.get(id=pk)

    context = {'location': location}
    return render(request, 'location.html', context)



def create_event(request):
    form = EventForm

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/all-events/')

    context = {'form': form}
    return render(request, 'create_event.html', context)



def create_location(request):
    form = LocationForm

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/all-locations/')

    context = {'form': form}
    return render(request, 'create_location.html', context)



def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('/all-events/')

    if request.method == 'POST':
        event.delete()
        return redirect('/all-events/')

    context = {'event': event, 'form': form}
    return render(request, 'edit_event.html', context)



def edit_location(request, pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(request.POST or None, instance=location)

    if form.is_valid():
        form.save()
        return redirect('/all-locations/')

    if request.method == 'POST':
        location.delete()
        return redirect('/all-locations/')

    context = {'location': location, 'form': form}
    return render(request, 'edit_location.html', context)

