from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100)

class Message(models.Model):
    room=models.CharField(max_length=10000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=10000)
    value=models.CharField(max_length=10000)