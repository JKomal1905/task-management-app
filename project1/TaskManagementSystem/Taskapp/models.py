from django.db import models

# Create your models here.
class TaskDetails(models.Model):
    Task_name=models.CharField(max_length=100)
    Task_status=models.BooleanField(default=False)