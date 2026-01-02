from django.contrib import admin
from django.contrib.auth.models import User

# Optional: extend User admin if needed
admin.site.unregister(User)  # Only if you customized
admin.site.register(User)
