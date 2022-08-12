from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def get_message(request):
    return Response({"name":"get the message"})


@api_view(['POST'])
def post_message(request):
    print(request.data)
    res = {'status':'success', 'data':request.data}
    return Response(res)