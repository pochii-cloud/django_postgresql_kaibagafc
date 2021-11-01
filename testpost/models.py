from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Joined(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField(max_length=1000)
    previous_club = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Joined'
