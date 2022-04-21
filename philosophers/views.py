from django.shortcuts import render
from rest_framework import generics
from Philosophers.models import Philosopher
from Philosophers.serializers import PhilosopherSerializer

# Create your views here.

class PhilosophersListView(generics.ListCreateAPIView):
    queryset = Philosopher.objects.all()
    serializer_class = PhilosopherSerializer

class PhilosopherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Philosopher.objects.all()
    serializer_class = PhilosopherSerializer