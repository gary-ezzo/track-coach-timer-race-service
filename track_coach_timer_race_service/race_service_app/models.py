from django.db import models

# Create your models here.
class Race(models.Model):
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50)
    