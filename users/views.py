from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from booking.models import Booking  # Import Booking model

# ==========================
# Home redirect based on role
# ==========================
@login_required
def home_redirect(request):
    if request.user.is_staff:
        # Admins go to Django admin
        return redirect('/admin/')
    else:
        # Normal users go to event list
        return redirect('event_list')

# ==========================
# User Registration
# ==========================
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

# ==========================
# User Login
# ==========================
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('event_list')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# ==========================
# User Logout
# ==========================
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# ==========================
# User Profile Page
# ==========================
@login_required
def profile(request):
    """
    Displays the logged-in user's profile information and their bookings.
    """
    user_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/profile.html', {'user_bookings': user_bookings})
