from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=TRUE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary =  models.TextField(default='Hello') 
    featured = models.BooleanField()