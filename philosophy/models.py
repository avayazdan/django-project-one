from django.db import models

# Create your models here.

class Philosophy(models.Model):  # inside the brackets is where its inheriting from
    """Philosophy is a child class of the Django `Model` class"""

    name = models.CharField(max_length=50)
    reigon_origin = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    founder = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    time_period = models.CharField(max_length=50)

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.title} - {self.branch}"