from select import POLLHUP
from rest_framework import serializers

from philosophers.models import Philosopher
from .models import Philosophy


class PhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Philosophy
        fields = '__all__'


class PhilosopherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Philosopher
        fields = '__all__'

        def create(self, data):
            Philosopher_data = data.pop("philosopher")

            Philosopher = Philosopher(**data)

            if Philosopher_data:
                Philosopher, _created = Philosopher.objects.get_or_create(
                    **Philosopher_data)
                Philosophy.Philosopher = Philosopher

            # Need to save to get the id
            Philosophy.save()

            return Philosophy

    def update(self, philosophy, data):
        Philosopher_data = data.pop("philosopher")
        Philosophy.image = data.get("image", Philosophy.image)

        if Philosopher_data:
            Philosopher, _created = Philosopher.objects.get_or_create(
                **Philosopher_data)
            Philosopher.author = Philosopher
            
        # save to the database
        Philosopher.save()

        # render to the api
        return Philosophy
