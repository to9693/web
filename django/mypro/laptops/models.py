from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length = 30)
    spec = models.TextField()
    price = models.CharField(max_length = 30)



class Program(models.Model):
    name = models.CharFeild(max_length = 20)
    spec = models.CharFeild(max_length = 30)

    laptops = models.ManyToManyField(Laptop, related_name = 'laptops')