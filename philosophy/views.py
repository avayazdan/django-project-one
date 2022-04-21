from rest_framework.views import APIview
from rest_framework.response import response 

from .models import Philosophy
from .serializers import ShowSerializer 

class showListView(APIview):
  def get(self, _request): 
        Philosophy = Show.objects.all()
        serialized_shows = ShowSeralizer(shows, many=True)
        return Response(serialized_shows.data)
      
class showDetailView(APIview): 
  def get(self, _request):
    
