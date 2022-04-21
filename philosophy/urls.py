from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view()),
    path('<str:pk>/', DetailView.as_view())
]