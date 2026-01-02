from django.contrib import admin
from .models import Event, Booking
from audit.models import AuditLog

admin.site.site_url = '/events/all/'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'available_seats', 'created_by')
    list_filter = ('date', 'created_by')
    search_fields = ('title', 'location', 'created_by__username')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at')
    list_filter = ('event', 'user')
    search_fields = ('user__username', 'event__title')

    def delete_model(self, request, obj):
        # ✅ AUDIT LOG
        AuditLog.objects.create(
            user=request.user,
            action=f"Admin deleted booking for user '{obj.user.username}' on event '{obj.event.title}'"
        )
        super().delete_model(request, obj)
