from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django_otp import user_has_device
from django_otp.middleware import is_verified


class Enforce2FAMiddleware(MiddlewareMixin):
    """
    Enforce 2FA site-wide:
    - If user is authenticated but has no OTP device -> force setup.
    - If user has OTP device but not verified in current session -> force 2FA login.
    """

    EXEMPT_PATH_PREFIXES = (
        "/static/",
        "/account/",  # allow whole 2FA flow pages
    )

    def process_request(self, request):
        # Skip exempt paths
        for prefix in self.EXEMPT_PATH_PREFIXES:
            if request.path.startswith(prefix):
                return None

        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            return None

        # Force setup if user has not configured 2FA device yet
        if not user_has_device(user):
            return redirect(reverse("two_factor:setup"))

        # Force OTP verification if not verified this session
        if not is_verified(user):
            return redirect(reverse("two_factor:login"))

        return None
