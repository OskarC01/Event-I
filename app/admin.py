from django.contrib import admin

from .models import UserProfile, Event, Location


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'id')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'approved', 'creator', 'id')
    ordering = ('date',)
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'manager', 'id')
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)


admin.site.site_header = "Event-I Admin"
admin.site.site_title = "Event-I Admin (Django)"
admin.site.index_title = "This is the Event-I Admin Page"
