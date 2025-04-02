from django.db import models

class SchoolData(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the primary key
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
