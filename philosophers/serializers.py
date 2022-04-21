from rest_framework import serializers
from .models import Philosophers, Show

class PhilosopherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Philosophers
        fields = '__all__'