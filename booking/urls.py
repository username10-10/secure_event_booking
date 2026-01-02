from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='event_create'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('all/', views.all_bookings, name='all_bookings'),
]
