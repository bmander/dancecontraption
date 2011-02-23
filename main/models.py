from django.db import models

# Create your models here.

class Dance(models.Model):
  name = models.CharField(max_length=255)

class Band(models.Model):
  name = models.CharField(max_length=255)

class Event(models.Model):
  date = models.DateField()
  dance = models.ForeignKey(Dance,blank=True)
  band = models.ForeignKey(Band,blank=True)
