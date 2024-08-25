from django.shortcuts import render

from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from rest_framework.filters import SearchFilter

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CarFilter
    search_fields = ['car_name']



