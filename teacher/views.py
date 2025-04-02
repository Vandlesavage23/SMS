from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Teacher

def add_teacher(request):
    if request.method == "POST":
        names = request.POST.get('names')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        qualification = request.POST.get('qualification')
        subjects_taught = request.POST.get('subjects_taught')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        teacher_image = request.FILES.get('teacher_image')

        teacher = Teacher.objects.create(
            names=names,
            teacher_id=teacher_id,
            gender=gender,
            date_of_birth=date_of_birth,
            qualification=qualification,
            subjects_taught=subjects_taught,
            joining_date=joining_date,
            mobile_number=mobile_number,
            email=email,
            address=address,
            teacher_image=teacher_image
        )
        messages.success(request, "Teacher added successfully")
        return redirect("teacher_list")
    
    return render(request, "teachers/add-teacher.html")

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teachers.html", {'teachers': teachers})

def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == "POST":
        teacher.names = request.POST.get('first_name')
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.qualification = request.POST.get('qualification')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.email = request.POST.get('email')
        teacher.address = request.POST.get('address')
        teacher.teacher_image = request.FILES.get('teacher_image') if request.FILES.get('teacher_image') else teacher.teacher_image
        teacher.save()
        return redirect("teacher_list")
    return render(request, "teachers/edit-teacher.html", {'teacher': teacher})

def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, "teachers/teacher-details.html", {'teacher': teacher})

def delete_teacher(request, slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher.delete()
        return redirect('teacher_list')
    return HttpResponseForbidden()
