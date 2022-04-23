from rest_framework import serializers
from .models import Philosopher
class PhilosopherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Philosopher
        fields = '__all__'