from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=15, blank=True,
        validators=[RegexValidator(
                regex='^[0-9\-\+]{9,15}$',
                message='Phone Number must be in +XXXXXXXXXXX format',
                code='invalid Phone format'
            )])
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, validators=[EmailValidator(message="Email wrong")], blank=True)

