from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
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
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            AuditLog.objects.create(user=user, action="User logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def user_logout(request):
    AuditLog.objects.create(user=request.user, action="User logged out")
    logout(request)
    return redirect('login')


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
