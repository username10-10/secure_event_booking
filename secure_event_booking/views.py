# secure_event_booking/views.py
from django.shortcuts import render
from django.http import HttpResponseBadRequest

# Test endpoints (temporary for testing custom error pages)
def test_400(request):
    return HttpResponseBadRequest("Bad Request")

def test_500(request):
    1 / 0  # triggers a server error

# Custom error handlers
def custom_400(request, exception=None):
    return render(request, 'errors/400.html', status=400)

def custom_403(request, exception=None):
    return render(request, 'errors/403.html', status=403)

def custom_404(request, exception=None):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)
