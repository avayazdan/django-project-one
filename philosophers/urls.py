from django.urls import path
from .views import PhilosophersListView, PhilosophersDetailView

urlpatterns = [
    path('', PhilosophersListView.as_view()),
    path('<str:pk>/', PhilosophersDetailView.as_view())
]