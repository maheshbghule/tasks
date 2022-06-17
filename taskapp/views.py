from asyncio import tasks
from email.mime import image
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from .serializers import taskSerializers
from .models import task
from .models import *
from rest_framework import status
# from django.http import HttpResponse


@api_view(['GET'])
def ShowAll(request):
    stu = task.objects.all()
    serializer = taskSerializers(stu, many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return Response(serializer.data)

@api_view(['GET'])
def ViewtaskName(request, name):
    stu = task.objects.get(name=name)
    serializer = taskSerializers(stu, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Addtask(request):
    serializer = taskSerializers(data=request.data)
    if serializer.is_valid():
     serializer.save()
     return Response({'msg':'Data Post'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def Updatetask(request, name):
  name = name
  stu = task.objects.get(name=name)
  serializer = taskSerializers(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Deletetask(request, name):
  name = name
  stu = task.objects.get(name=name)
  stu.delete()
  return Response({'msg':'Data Deleted'})