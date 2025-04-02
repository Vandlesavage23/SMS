from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    # Other URL patterns...
    path('admin/dashboard/', views.admin_dashboard, name='admin-dashboard'), 
    
]
