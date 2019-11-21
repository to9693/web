from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length = 30)
    spec = models.TextField()
    price = models.CharField(max_length = 30)