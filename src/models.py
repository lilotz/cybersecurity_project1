from django.db import models

# Create your models here.
class Diaries(models.Model):
  author = models.CharField(max_length=50)
  entry = models.TextField()

class User(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)