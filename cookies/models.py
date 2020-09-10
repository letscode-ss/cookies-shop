from django.db import models

# Create your models here.
class Cookie(models.Model):
    SIZE_OPTIONS = [('S','Small'), ('L','Large')]
    name = models.CharField(max_length=100)
    calories = models.IntegerField(null=True)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=1, choices=SIZE_OPTIONS, blank=True)
    description = models.TextField(blank=True)
    imagepath = models.CharField(max_length=200)