from rest_framework import serializers
from projects.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('id', 'project_title', 'project_description', 'project_progress', 'create_by', 'create_at','updated_at')