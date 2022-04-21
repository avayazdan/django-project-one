from requests import Response
from rest_framework.views import APIview
from rest_framework.response import response 

from .models import Philosophy
from .serializers import PhilosophySerializer 

class ListView(APIview):
  def get(self, _request): 
        Philosophy = Philosophy.objects.all()
        serialized_philosophy = PhilosophySerializer(Philosophy, many=True)
        return Response(serialized_philosophy.data)
      
class DetailView(APIView):
    def get(self, _request, pk):
        Philosophy = Philosophy.objects.get(id=pk)
        serialized_philosophy = PhilosophySerializer(Philosophy, many=False)
        return Response(serialized_philosophy.data)
      
def put (self, request, pk):
    Philosophy = Philosophy.objects.get(id=ik)
    serialized_philosophy = PhilosophySerializer(Philosophy, data=request.data)
  
    if serialized_philosophy.is_valid():
      serialized_philosophy.save()
      return Response(serialized_philosophy.data, status=status.HTTP_200_OK)
    
  return Response(serialzed_philosophy.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, _request, pk):
  