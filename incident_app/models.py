from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('individual', 'Individual'),
    ('enterprise', 'Enterprise'),
    ('government', 'Government')
)

PRIORITY_CHOICES = (
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('high', 'HIGH')
)

STATUS_CHOICES = (
    ('open', 'OPEN'),
    ('in progress', 'IN PROGRESS'),
    ('closed', 'CLOSED'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=15, default=0)
    address = models.CharField(max_length=60)
    pin = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.phone


class Incident(models.Model):
    incident_id = models.CharField(max_length=20, primary_key=True)
    incident_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    incident_details = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="LOW")
    incident_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.incident_id
