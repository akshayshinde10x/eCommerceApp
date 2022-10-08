from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    imgPath = models.CharField(max_length=100)


class Order(models.Model):
    name = models.CharField(max_length=50)
    number = models.BigIntegerField()
    email = models.EmailField(max_length=20)
    degree = models.CharField(max_length=50)
    gradYear = models.IntegerField()