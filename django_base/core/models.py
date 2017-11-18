from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Contact(models.Model):
    email = models.EmailField(blank=True, max_length=120)
    interests = JSONField(blank=True, null=True)