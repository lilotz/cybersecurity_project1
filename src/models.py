from django.db import models

# Create your models here.
class Diaries(models.Model):
  author = models.CharField(max_length=50)
  entry = models.TextField()