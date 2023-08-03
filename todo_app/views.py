from django.shortcuts import render
from rest_framework.response import Response
from .models import ToDo
from .serializer import ToDoSerializer
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


# Create your views here.
class ToDoList(GenericAPIView,ListModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
class ToDoCreate(GenericAPIView,CreateModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

