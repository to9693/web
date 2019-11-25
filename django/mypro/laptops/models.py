from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length = 30)
    price = models.CharField(max_length = 30)



class Program(models.Model):
    name = models.CharField(max_length = 20)
    spec = models.CharField(max_length = 30)


class Graphic(models. Model):
    graphic = models.TextField(default="")


class Info(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete = models.CASCADE)
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    graphic = models.ForeignKey(Graphic, on_delete = models.CASCADE)