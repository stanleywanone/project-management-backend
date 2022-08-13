from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from projectsApp.models import Projects
from projectsApp.serializers import ProjectsSerializer

# Create your views here.
@api_view(['GET'])
def get_projects(request):
    projects = Projects.objects.all()
    projects_serializer = ProjectsSerializer(projects, many=True)

    return JsonResponse(projects_serializer.data, safe=False)

@api_view(['POST'])
def add_project(request):
    new_project_data = JSONParser().parse(request)
    new_project_serializer = ProjectsSerializer(data=new_project_data)
    if new_project_serializer.is_valid():
        new_project_serializer.save()
        return JsonResponse("Add Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)