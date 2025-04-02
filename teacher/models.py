from django.db import models
from django.utils.text import slugify

class Teacher(models.Model):
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