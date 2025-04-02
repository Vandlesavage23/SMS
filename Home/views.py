from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def school_login(request):
    """
    View for the school login page.
    """
    return render(request, 'tenants/login.html')


def dashboard_view(request):
    """
    View for the dashboard page.
    """
    return render(request, 'tenants/dashboard.html')