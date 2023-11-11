# Django
from django.db import models

class Calification(models.Model):
    name = models.CharField(max_length=250)
