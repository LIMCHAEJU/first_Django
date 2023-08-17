from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    work = models.CharField(max_length=400, default='null')
    isComplete = models.BooleanField(default=False)