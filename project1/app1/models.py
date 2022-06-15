from importlib.metadata import files
from unicodedata import name
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    file = models.FileField(upload_to='resume/',null=True, blank=True)