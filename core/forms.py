from django import forms
from .models import ThreatIncident

class ThreatIncidentForm(forms.ModelForm):
    class Meta:
        model = ThreatIncident
        fields = ['title', 'detector', 'access_vector', 'severity', 'description', 'is_false_positive']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Incident Title'}),
            'detector': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., NIDS, Firewall'}),
            'access_vector': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Network, Phishing Link'}),
            'severity': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Provide brief threat details...'}),
            'is_false_positive': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }