from email.policy import default
from django.db import models

# Create your models here.

class Task(models.Model):
    # Here the tasks are defined for the database schema
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title