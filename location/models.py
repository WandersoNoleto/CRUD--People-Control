from django.db import models


class Location(models.Model):
    address    = models.CharField(max_length=150, verbose_name="Endereço")
    complement = models.CharField(max_length=250, verbose_name="Complemento")
    city       = models.CharField(max_length=50,  verbose_name="Cidade")
    region     = models.CharField(max_length=50,  verbose_name="Estado/Província")
    country    = models.CharField(max_length=50,  verbose_name="País")
    latitude   = models.FloatField(null=True,   verbose_name="Latitude")
    longitude  = models.FloatField(null=True,   verbose_name="Longitude")

    def __str__(self):
        return self.addres