from django.db import models

# Create your models here.

class Clothing(models.Model):
  jackets = models.CharField(max_length=255)
  shirts = models.CharField(max_length=255)
  pants = models.CharField(max_length=255)
  shoes = models.CharField(max_length=255)
