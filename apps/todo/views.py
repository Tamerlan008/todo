from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


# Create your views here.


class TaskViewSet(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class CreateTaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class RetrieveTaskAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class UpdateTaskAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class DeleteTaskAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers