from django.shortcuts import render
from rest_framework.response import Response
from .models import ToDo
from .serializer import ToDoSerializer
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin,ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin



#
# # Create your views here.
# class ToDoList(GenericAPIView,ListModelMixin):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)
#
# class ToDoCreate(GenericAPIView,CreateModelMixin):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args,**kwargs)
#
# class ToDoSpecific(GenericAPIView,RetrieveModelMixin):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)
#
# class ToDoUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)
#
# class ToDoDelete(GenericAPIView, DestroyModelMixin):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request,*args,**kwargs)

class ToDoListCreate(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class ToDoSpecificUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)
