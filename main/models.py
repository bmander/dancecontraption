from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  facebook = models.OneToOneField('FacebookLink',blank=True,null=True)

  def display_name(self):
    ret = ""
    if self.user.first_name and self.user.first_name!='':
        ret = ret+self.user.first_name

    if self.user.last_name and self.user.last_name!='':
        ret = ret+" "+self.user.last_name

    if ret!='':
        return ret
    else:
        return self.user.username

class FacebookLink(models.Model):
  oauth_code = models.CharField(max_length=255)
  access_token = models.CharField(max_length=255)
  account_id = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  link = models.CharField(max_length=255)

class Person(models.Model):
  name = models.CharField(max_length=255)
  name_normalized = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

class Dance(models.Model):
  name = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

class Band(models.Model):
  name = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

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
  dance = models.ForeignKey(Dance)
  band = models.ForeignKey(Band,null=True,blank=True)
  caller = models.ForeignKey(Person,null=True,blank=True)

  def __unicode__(self):
    return "id:%s date:%s dance_id:%s band_id:%s"%(self.id, self.date,self.dance_id,self.band_id)

class Homeship(models.Model):
  user = models.ForeignKey(User, related_name="homeships")
  dance = models.ForeignKey(Dance)

class Attendship(models.Model):
  user = models.ForeignKey(User, related_name="attendships")
  event = models.ForeignKey(Event, related_name="attendships")

  date = models.DateField(null=True) # a copy of event.date, so we can sort eventships

  def __unicode__(self):
    return "user_id:%s event_id:%s"%(self.user_id, self.event_id)
