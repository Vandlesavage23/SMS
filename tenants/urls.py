from django.urls import path
from . import views

app_name = 'tenants'

urlpatterns = [
    path('', views.list_tenants, name='list_tenants'),
    path('create/', views.create_tenant, name='create_tenant'),
    path('<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
]
