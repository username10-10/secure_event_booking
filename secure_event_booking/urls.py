from django.contrib import admin
from django.urls import path, include
from users.views import home_redirect
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('users/', include('users.urls')),
    path('events/', include('booking.urls')),
    path('audit/', include('audit.urls')),
      path('', lambda request: redirect('all_bookings')),  # root redirects to all bookings
]
handler400 = 'secure_event_booking.views.handler400'
handler403 = 'secure_event_booking.views.handler403'
handler404 = 'secure_event_booking.views.handler404'
handler500 = 'secure_event_booking.views.handler500'

