from django import forms
from .models import Tenant

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'subdomain', 'logo_url', 'contact', 'address', 'email']
