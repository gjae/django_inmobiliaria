from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
    firstname = models.CharField('Nombre', max_length=60)
    lastname = models.CharField('Nombre', max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return '{0} {1}'.format(
            self.lastname,
            self.firstname
        )

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40)
    phone_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='provinces')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40)
    province = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name