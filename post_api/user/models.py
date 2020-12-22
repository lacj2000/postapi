from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=128)
    suite = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    def __str__(self):
        return self.street


class Profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.ForeignKey('Address',related_name='address',on_delete=models.CASCADE) 
    def __str__(self):
        return self.name