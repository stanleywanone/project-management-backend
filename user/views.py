from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
# Create your views here.

@api_view(['GET'])
def get_users(request):
    users = get_user_model().objects.first().__dict__
    print(users)
    return JsonResponse({'message':'ok'})

@api_view(['POST'])
def create_user(request):
    user = JSONParser().parse(request)
    print(user)
    new_user = get_user_model().objects.create_user(username=user['username'], email=user['email'], password=user['password'])
    new_user.save()
    return JsonResponse({'message':'ok'})