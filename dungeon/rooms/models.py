from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 255)
    width = models.IntegerField()
    length = models.IntegerField()

class Door(models.Model):
    wall = models.CharField(max_length = 50)
    position = models.IntegerField()
    room = models.CharField(max_length = 50)