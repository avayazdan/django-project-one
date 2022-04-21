from django.urls import path
from .views import PhilosophyListView

urlpatterns = [
    path('', PhilosophyListView.as_view()),
]