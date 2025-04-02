from django.contrib import admin
from .models import Student, Parent

class ParentInline(admin.TabularInline):
    model = Parent
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_class', 'admission_number')
    search_fields = ('first_name', 'last_name', 'student_id')
    inlines = [ParentInline]

admin.site.register(Student, StudentAdmin)
