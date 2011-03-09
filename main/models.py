from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  facebook = models.OneToOneField('FacebookLink',blank=True,null=True)

class FacebookLink(models.Model):
  oauth_code = models.CharField(max_length=255)
  access_token = models.CharField(max_length=255)
  account_id = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  link = models.CharField(max_length=255)

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

class Homeship(models.Model):
  user = models.ForeignKey(User, related_name="homeships")
  dance = models.ForeignKey(Dance)
