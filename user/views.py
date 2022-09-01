from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def get_users(request):
    users = get_user_model().objects.first().__dict__
    return JsonResponse({'status':200})

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
    user = JSONParser().parse(request)
    try:
        new_user = get_user_model().objects.create_user(username=user['username'], email=user['email'], password=user['password'])
        if new_user:
            new_user.save()
            return Response({'status':'success'},status=status.HTTP_200_OK)
    except:
        return Response({'status':'failed'},status=status.HTTP_400_BAD_REQUEST)