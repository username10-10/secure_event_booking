from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AuditLog

@login_required
def audit_logs(request):
    """Admins view audit logs."""
    if not request.user.is_staff:
        messages.error(request, "Admins only.")
        return redirect('event_list')

    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})
