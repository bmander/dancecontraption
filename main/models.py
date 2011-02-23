from django.db import models

# Create your models here.

class Person(models.Model):
  name = models.CharField(max_length=255)

class Dance(models.Model):
  name = models.CharField(max_length=255)

class Band(models.Model):
  name = models.CharField(max_length=255)

class Instrument(models.Model):
  name = models.CharField(max_length=255)

class BandMember(models.Model):
  person = models.ForeignKey(Person)
  band = models.ForeignKey(Band, related_name='members')

class BandInstrument(models.Model):
  instrument = models.ForeignKey(Instrument)
  member = models.ForeignKey(BandMember, related_name='instruments')

  def __unicode__(self):
    return self.instrument.name

class Event(models.Model):
  date = models.DateField()
  dance = models.ForeignKey(Dance,blank=True)
  band = models.ForeignKey(Band,blank=True)
