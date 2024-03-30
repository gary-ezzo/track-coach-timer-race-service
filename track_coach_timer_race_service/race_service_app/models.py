from django.db import models

# Create your models here.
class Race(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50, default='Default Title')
    timer_user_id = models.CharField(max_length=50, default='defaultuserid')

class Runner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Split(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="split")
    lap_number = models.IntegerField()
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE, related_name="split")
    
    