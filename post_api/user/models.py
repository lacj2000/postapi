from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=128)
    suite = models.IntegerField()
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=9)

class Profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    adress = models.ForeignKey('Address',on_delete=models.CASCADE)