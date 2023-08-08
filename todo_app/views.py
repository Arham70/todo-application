from django.shortcuts import render
from rest_framework.response import Response
from .models import ToDo
from .serializer import ToDoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .Exception import NotFoundException


@api_view(['GET'])
def GetApi(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            try:
                TODO = ToDo.objects.get(id=id)
            except ToDo.DoesNotExist:
                raise NotFoundException
            serializer = ToDoSerializer(TODO)
            return Response(serializer.data)

        TODO = ToDo.objects.all()
        serializer = ToDoSerializer(TODO, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def CreateApi(request):
    if request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data uploaded'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'Data not uploaded'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def UpdateApi(request, pk=None):
    if request.method == 'PUT':
        id = pk
        if id is not None:
            try:
                TODO = ToDo.objects.get(pk=id)
            except ToDo.DoesNotExist:
                raise NotFoundException
            serializer = ToDoSerializer(TODO, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'U cannot update data because u do not put id'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def PartialUpdateApi(request, pk=None):
    if request.method == 'PATCH':
        id = pk
        if id is not None:
            try:
                TODO = ToDo.objects.get(pk=id)
            except ToDo.DoesNotExist:
                raise NotFoundException
            serializer = ToDoSerializer(TODO, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Partial Data Updated'})
            return Response(serializer.errors)
        return Response({'msg': 'U cannot update data because u do not put id'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def DeleteApi(request, pk=None):
    if request.method == 'DELETE':
        id = pk
        if id is not None:
            try:
                TODO = ToDo.objects.get(pk=id)
            except ToDo.DoesNotExist:
                raise NotFoundException
            TODO.delete()
            return Response({'msg': 'Data Deleted'})
        return Response({'msg': 'U cannot Delete data because u cannot put id'},
                        status=status.HTTP_400_BAD_REQUEST)
