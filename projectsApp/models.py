from django.db import models
import uuid

# Create your models here.
class Projects(models.Model):
    id = models.CharField(primary_key=True,  max_length=225)
    project_title = models.CharField(max_length=225)
    project_description = models.CharField(max_length=225)
    project_progress = models.CharField(max_length=225)
    project_priority = models.CharField(max_length=225, null=True)
    project_type = models.CharField(max_length=225, null=True)
    created_by = models.CharField(max_length=225, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   