from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'attachment']
        widgets = {
            'service_type': forms.Select(),
            'description': forms.Textarea(),
            'attachment': forms.ClearableFileInput(),
        }
