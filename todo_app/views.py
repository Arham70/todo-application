from django.shortcuts import render
from rest_framework.response import Response
from .models import ToDo
from .serializer import ToDoSerializer,ToDoDocumentationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .Exception import NotFoundException
from drf_yasg.utils import swagger_auto_schema
# from .serializer import ExcludeFieldsInspector, CustomSerializerInspector




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


@swagger_auto_schema(
    methods=['post'],
    request_body=ToDoDocumentationSerializer
)
@api_view(['POST'])
def CreateApi(request):
    if request.method == 'POST':
        request_data = request.data.copy()
        request_data.pop('created_at', None)
        request_data.pop('completed', None)

        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data uploaded'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['put'],
    request_body=ToDoSerializer,
    responses={
        status.HTTP_201_CREATED: 'Data uploaded',
        status.HTTP_400_BAD_REQUEST: 'Data not uploaded',
    },
)
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


@swagger_auto_schema(
    methods=['patch'],
    request_body=ToDoSerializer,
    responses={
        status.HTTP_201_CREATED: 'Data uploaded',
        status.HTTP_400_BAD_REQUEST: 'Data not uploaded',
    },
)
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
