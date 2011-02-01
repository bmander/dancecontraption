from django.db import models

# Create your models here.

class Dance(models.Model):
  name = models.CharField(max_length=255)
