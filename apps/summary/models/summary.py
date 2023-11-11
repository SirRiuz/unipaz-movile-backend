# Django
from django.db import models

class Summary(models.Model):
    name = models.CharField(max_length=250)
