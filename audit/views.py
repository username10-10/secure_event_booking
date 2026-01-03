from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import AuditLog

@login_required
def audit_logs(request):
    if not request.user.is_staff:
        AuditLog.objects.create(
            user=request.user,
            action="Suspicious activity: non-admin attempted to access audit logs"
        )
        raise PermissionDenied

    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'audit/audit_logs.html', {'logs': logs})
