from django.db import models


# Create your models here.
class ToDo(models.Model):
    # id = models.AutoField
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField()
    completed = models.BooleanField()
