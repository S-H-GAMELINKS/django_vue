from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
from .serializers import TodoSerializer

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer