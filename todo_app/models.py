from django.db import models
from datetime import datetime


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)
