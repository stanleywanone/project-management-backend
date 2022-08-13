from django.db import models

# Create your models here.

class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_title = models.CharField(max_length=50)
    project_description = models.CharField(max_length=225)
    project_progress = models.CharField(max_length=50)
    create_by = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
