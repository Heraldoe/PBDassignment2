from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()