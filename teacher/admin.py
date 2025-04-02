from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('names', 'teacher_id', 'gender', 'date_of_birth', 'qualification', 'experience', 'joining_date', 'mobile_number', 'email','address', 'teacher_image')
    search_fields = ('names', 'teacher_id', 'email')
    list_filter = ('gender', 'qualification')
    readonly_fields = ('teacher_image',)
