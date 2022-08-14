from rest_framework import serializers
from projectsApp.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('id', 'project_title', 'project_description', 'project_progress', 'created_by', 'created_at','updated_at', 'project_priority')