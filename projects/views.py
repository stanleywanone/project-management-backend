from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from projects.models import Projects
from projects.serializers import ProjectsSerializer
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def get_message(request):
    projects = Projects.objects.all()
    projects_serializer = ProjectsSerializer(projects, many=True)
    # return Response({"name":"get the message"})
    return JsonResponse(projects_serializer.data, safe=False)


@api_view(['POST'])
def post_message(request):
    project_data = JSONParser().parse(request)
    projects_serializer = ProjectsSerializer(data=project_data)
    if projects_serializer.is_valid():
        projects_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)