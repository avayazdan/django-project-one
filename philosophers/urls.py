from django.urls import path
from .views import PhilosophersListView, PhilosopherDetailView

urlpatterns = [
    path('', PhilosophersListView.as_view()),
    path('<str:pk>/', PhilosopherDetailView.as_view())
]