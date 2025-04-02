from django.contrib import admin
from .models import Tenant, Parent, Student, Teacher, Class, Course, Grade, Fee, Payment

admin.site.register(Tenant)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Fee)
admin.site.register(Payment)
