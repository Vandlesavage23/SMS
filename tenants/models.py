from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.utils import timezone

# Choices for gender, roles, and other fields
gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

role_choices = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
    ('parent', 'Parent'),
)

service_status_choices = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

# Tenant class to represent a school or institution
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255, unique=True)
    logo_url = models.FileField(upload_to='logo/', editable=True, blank=True, null=True)
    contact = models.CharField(max_length=255, editable=True, blank=True, null=True)
    address = models.CharField(max_length=255, editable=True, blank=True, null=True)
    email = models.EmailField(max_length=255, editable=True, blank=True, null=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


# Parent Model to link students
class Parent(TenantAwareModel):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"


# Student model linked to the parent
class Student(TenantAwareModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gender_choices)
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"


# Teacher model
class Teacher(TenantAwareModel):
    names = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=200)
    subjects_taught = models.CharField(max_length=255, default='Default Subject')
    experience = models.CharField(max_length=200)
    joining_date = models.DateField()
    user_name = models.CharField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField()
    teacher_image = models.ImageField(upload_to='teachers/', blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.names}-{self.teacher_id}")
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.names} ({self.teacher_id})"


# Class model to represent student classes
class Class(TenantAwareModel):
    name = models.CharField(max_length=255)
    grade_level = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name


# Course model to represent subjects taught in school
class Course(TenantAwareModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name


# Grades for each student in each course
class Grade(TenantAwareModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_recorded = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {self.course}"


# Fee model for each student
class Fee(TenantAwareModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    fee_type = models.CharField(max_length=255)
    due_date = models.DateField()
    paid_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.fee_type} - {self.amount}"


# Payment model to record fee payments
class Payment(TenantAwareModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    payment_date = models.DateField(default=timezone.now)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.amount_paid} - {self.payment_date}"
