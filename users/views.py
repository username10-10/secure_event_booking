from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.urls import reverse

from booking.models import Booking
from audit.models import AuditLog
from .forms import UserRegisterForm


def is_business_admin(user):
    return user.groups.filter(name='BUSINESS_ADMIN').exists()


@login_required
def home_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    elif is_business_admin(request.user):
        return redirect('business_dashboard')
    else:
        return redirect('event_list')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully.")
            # Redirect to 2FA login
            return redirect(reverse("two_factor:login"))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    # Legacy login route -> redirect to django-two-factor-auth login
    return redirect(reverse("two_factor:login"))


@login_required
def user_logout(request):
    AuditLog.objects.create(user=request.user, action="User logged out")
    logout(request)
    return redirect(reverse("two_factor:login"))


@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'user_bookings': bookings})


@login_required
@user_passes_test(is_business_admin)
def business_admin_dashboard(request):
    users = User.objects.all()
    bookings = Booking.objects.all()
    return render(request, 'business/dashboard.html', {
        'users': users,
        'bookings': bookings
    })
