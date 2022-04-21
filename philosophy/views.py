from .models import Philosophy
from .serializers import PhilosophySerializer
from rest_framework import generics

class ListView(generics.ListCreateAPIView):
  queryset = Philosophy.objects.all()
  serializer_class = PhilosophySerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Philosophy.objects.all()
    serializer_class = PhilosophySerializer
  
  

