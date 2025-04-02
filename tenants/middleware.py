from django.db import connection
from .models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        school_slug = request.GET.get('school', None)  # Or extract school from session/user
        if school_slug:
            tenant = Tenant.objects.get(school__slug=school_slug)
            connection.set_schema(tenant.schema_name)
        response = self.get_response(request)
        return response
