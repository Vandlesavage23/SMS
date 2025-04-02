from django.shortcuts import render, get_object_or_404
from .models import Tenant, Student, Teacher, Parent
from django.http import HttpResponse
from django.shortcuts import redirect

# View to list all tenants
def list_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/list_tenants.html', {'tenants': tenants})

# View to create a new tenant
def create_tenant(request):
    if request.method == 'POST':
        name = request.POST['name']
        subdomain = request.POST['subdomain']
        logo_url = request.FILES.get('logo_url', None)
        contact = request.POST['contact']
        email = request.POST['email']
        tenant = Tenant.objects.create(name=name, subdomain=subdomain, logo_url=logo_url, contact=contact, email=email)
        return redirect('tenants:list_tenants')
    return render(request, 'tenants/create_tenant.html')

# View for a specific tenant (detail view)
def tenant_detail(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    students = Student.objects.filter(tenant=tenant)
    teachers = Teacher.objects.filter(tenant=tenant)
    return render(request, 'tenants/tenant_detail.html', {'tenant': tenant, 'students': students, 'teachers': teachers})
