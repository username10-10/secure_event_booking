from django.contrib import admin
from .models import Event, Booking

admin.site.site_url = '/events/all/'
# Event admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'available_seats', 'created_by')
    list_filter = ('date', 'created_by')
    search_fields = ('title', 'location', 'created_by__username')

# booking/admin.py
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at')  # now exists
    list_filter = ('event', 'user')
    search_fields = ('user__username', 'event__title')
