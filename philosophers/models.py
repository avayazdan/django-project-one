from django.db import models

# Create your models here.

class Philosopher(models.Model):  # inside the brackets is where its inheriting from

    name = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=50)
    works = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    time_period = models.CharField(max_length=50)

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.name} - {self.branch}"
      