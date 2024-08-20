from django.contrib import admin
from incident_app.models import Incident, UserProfile

admin.site.register(UserProfile)
admin.site.register(Incident)