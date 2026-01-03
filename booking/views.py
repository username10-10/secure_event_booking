from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Event, Booking
from .forms import EventForm
from audit.models import AuditLog  # ✅ central audit log


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
    if not request.user.is_staff:
        # 🚨 Suspicious activity: non-admin trying to create event
        AuditLog.objects.create(
            user=request.user,
            action="Suspicious activity: non-admin attempted to create event"
        )
        raise PermissionDenied

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()

            # ✅ Admin action logged
            AuditLog.objects.create(
                user=request.user,
                action=f"Admin created event '{event.title}'"
            )

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

    # ✅ Booking action logged
    AuditLog.objects.create(
        user=request.user,
        action=f"User booked event '{event.title}'"
    )

    messages.success(request, f"🎉 You booked '{event.title}' successfully!")

    if request.user.is_staff:
        return redirect('all_bookings')
    return redirect('my_bookings')


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # 🚨 IDOR + RBAC protection with logging
    if not request.user.is_staff and booking.user != request.user:
        AuditLog.objects.create(
            user=request.user,
            action="Suspicious activity: unauthorized booking cancellation attempt"
        )
        raise PermissionDenied

    event = booking.event
    booked_user = booking.user

    # Restore seat
    event.available_seats += 1
    event.save()

    # ✅ Audit logging for cancellation
    if request.user.is_staff:
        AuditLog.objects.create(
            user=request.user,
            action=f"Admin cancelled booking for user '{booked_user.username}' on event '{event.title}'"
        )
    else:
        AuditLog.objects.create(
            user=request.user,
            action=f"User cancelled own booking on event '{event.title}'"
        )

    booking.delete()

    messages.success(request, f"Booking for '{event.title}' canceled.")

    if request.user.is_staff:
        return redirect('all_bookings')
    return redirect('my_bookings')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


# ==========================
# Admin Only Views
# ==========================

@login_required
def all_bookings(request):
    if not request.user.is_staff:
        # 🚨 Suspicious activity: non-admin accessing admin bookings
        AuditLog.objects.create(
            user=request.user,
            action="Suspicious activity: non-admin attempted to access all bookings"
        )
        raise PermissionDenied

    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'booking/all_bookings.html', {'bookings': bookings})
