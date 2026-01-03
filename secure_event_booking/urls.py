from django.contrib import admin
from django.urls import path, include
from users.views import home_redirect
from django.shortcuts import redirect
from secure_event_booking.views import test_400, test_500  # Import these for testing

handler400 = 'secure_event_booking.views.custom_400'
handler403 = 'secure_event_booking.views.custom_403'
handler404 = 'secure_event_booking.views.custom_404'
handler500 = 'secure_event_booking.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('users/', include('users.urls')),
    path('events/', include('booking.urls')),
    path('audit/', include('audit.urls')),
    path('', lambda request: redirect('all_bookings')),  # root redirects to all bookings
 path('test-500/', test_500),
    path('test-400/', test_400),
]
