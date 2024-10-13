from django import forms
from customers.models import ServiceRequest

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']
