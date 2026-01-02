from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking
from .forms import EventForm
from django.utils import timezone

# ==========================
# Event Views
# ==========================

@login_required
def event_list(request):
    """Show all events. Admins and users see the same event list."""
    events = Event.objects.all()
    return render(request, 'booking/event_list.html', {'events': events})

@login_required
def create_event(request):
    """Allow admins to create a new event."""
    if not request.user.is_staff:
        messages.error(request, "Admins only.")
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, "Event created successfully.")
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'booking/event_create.html', {'form': form})

# ==========================
# Booking Views
# ==========================

@login_required
def book_event(request, event_id):
    """Book an event. Admins redirected to all bookings; users to their bookings."""
    event = get_object_or_404(Event, id=event_id)

    if event.available_seats <= 0:
        messages.error(request, "No seats available.")
        return redirect('event_list')

    if Booking.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "You already booked this event.")
        return redirect('event_list')

    Booking.objects.create(user=request.user, event=event)
    event.available_seats -= 1
    event.save()
    messages.success(request, f"🎉 You booked '{event.title}' successfully!")

    # Redirect based on role
    if request.user.is_staff:
        return redirect('all_bookings')
    else:
        return redirect('my_bookings')

@login_required
def cancel_booking(request, booking_id):
    """Cancel a booking. Admins can cancel any; users only their own."""
    booking = get_object_or_404(Booking, id=booking_id)

    # Permission check
    if not request.user.is_staff and booking.user != request.user:
        messages.error(request, "You cannot cancel this booking.")
        return redirect('event_list')

    # Save details BEFORE delete
    event = booking.event
    booked_user = booking.user

    # Restore seat
    event.available_seats += 1
    event.save()

    # ✅ AUDIT LOG (All cancellations)
    from audit.models import AuditLog
    if request.user.is_staff:
        # Admin cancels someone else's booking
        AuditLog.objects.create(
            user=request.user,
            action=f"Admin cancelled booking for user '{booked_user.username}' on event '{event.title}'"
        )
    else:
        # User cancels their own booking
        AuditLog.objects.create(
            user=request.user,
            action=f"User '{request.user.username}' canceled their own booking on event '{event.title}'"
        )

    # Delete the booking after logging
    booking.delete()

    messages.success(request, f"Booking for '{event.title}' canceled.")

    # Redirect based on role
    if request.user.is_staff:
        return redirect('all_bookings')
    else:
        return redirect('my_bookings')



@login_required
def my_bookings(request):
    # Use 'created_at' instead of 'booked_at'
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

# ==========================
# Admin Only Views
# ==========================

@login_required
def all_bookings(request):
    if not request.user.is_staff:
        messages.error(request, "Admins only.")
        return redirect('event_list')

    # Use 'created_at' instead of 'booked_at'
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'booking/all_bookings.html', {'bookings': bookings})


# ==========================
# Audit Log View (Optional)
# ==========================

@login_required
def audit_logs(request):
    """Admins view audit logs."""
    if not request.user.is_staff:
        messages.error(request, "Admins only.")
        return redirect('event_list')

    # Replace with your AuditLog model if you have one
    from audit.models import AuditLog
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})
