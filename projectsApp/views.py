from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from projectsApp.models import Projects
from projectsApp.serializers import ProjectsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_projects(request):
    try:  
        projects = Projects.objects.all()
        projects_serializer = ProjectsSerializer(projects, many=True)
        return Response({'status':'success', 'data':projects_serializer.data})
    except:
        print('no')
        return Response({'status':401}, status=status.HTTP_401_UNAUTHORIZED)
  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_project(request):
    new_project_data = JSONParser().parse(request)
    new_project_serializer = ProjectsSerializer(data=new_project_data)
    if new_project_serializer.is_valid():
        new_project_serializer.save()
        return JsonResponse({'status':'success'}, safe=False)
    return JsonResponse({'status':'failed'}, safe=False)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updated_project(request, pk):
    try: 
        get_project = Projects.objects.get(id=pk)
    except Projects.DoesNotExist: 
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    updated_project_data = JSONParser().parse(request)
    updated_project_serializer = ProjectsSerializer(get_project, data=updated_project_data)
    if updated_project_serializer.is_valid():
        updated_project_serializer.save()
        return JsonResponse ({'status':'success'}, safe=False)
    return JsonResponse({'status':'failed'}, safe=False)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updated_drag_project(request, pk):
    try:
        get_project = Projects.objects.get(id=pk)
    except Projects.DoesNotExist:
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    updated_project_data = JSONParser().parse(request)
    updated_project_serializer = ProjectsSerializer(get_project, data={'project_progress':updated_project_data}, partial=True)
    if updated_project_serializer.is_valid():
        updated_project_serializer.save()
        return JsonResponse ({'status':'success'}, safe=False)
    return JsonResponse({'status':'failed'}, safe=False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    try:
        get_project = Projects.objects.get(id=pk)
    except Projects.DoesNotExist:
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)
    get_project.delete()
    return JsonResponse({'status':'success'}, safe=False)