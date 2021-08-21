from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

