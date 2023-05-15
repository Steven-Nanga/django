from django.db import models
from datetime import datetime
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    position = models.CharField(max_length=30)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name 
