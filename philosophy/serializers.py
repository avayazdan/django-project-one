from select import POLLHUP
from rest_framework import serializers
from .models import Philosophy

class PhilosophySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Philosophy
        fields = '__all__'