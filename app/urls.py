from django.urls import path

from .views import (
    mainpage, event, all_events, 
    location, create_event, create_location, 
    all_locations, edit_event, edit_location,
)


urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('event/<int:pk>/', event, name='event'),
    path('all-events/', all_events, name='all_events'),
    path('location/<int:pk>/', location, name='location'),
    path('create-event/', create_event, name='create_event'),
    path('create-location/', create_location, name='create_location'),
    path('all-locations/', all_locations, name='all_locations'),
    path('edit-event/<int:pk>/', edit_event, name='edit_event'),
    path('edit-location/<int:pk>/', edit_location, name='edit_location'),
]
