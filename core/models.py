from django.db import models
from django.contrib.auth.models import User

class ThreatIncident(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    
    title = models.CharField(max_length=200, help_text="e.g., Brute Force Attack, Phishing Attempt")
    detector = models.CharField(max_length=100, default='Signature Matching', help_text="e.g., Firewall, NIDS, Antivirus")
    access_vector = models.CharField(max_length=100, default='Network', help_text="e.g., Local, Network, Physical")
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='MEDIUM')
    description = models.TextField()
    is_false_positive = models.BooleanField(default=False, verbose_name="Mark as False Positive")
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.severity})"