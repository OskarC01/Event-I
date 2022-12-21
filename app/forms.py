from django import forms
from django.forms import ModelForm

from .models import Event, Location


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'image', 'location', 'description',
                  'event_type', 'age_restriction', 'entry_fee', 'maximum_participants')


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address', 'image', 'email', 'phone', 'description')
