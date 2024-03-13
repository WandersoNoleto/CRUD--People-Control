from django.db import models


class TouristSpot(models.Model):
    name        = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    resources   = models.TextField(verbose_name="Recursos")
    city        = models.CharField(max_length=150, verbose_name="Cidade")
    state       = models.CharField(max_length=150, verbose_name="Estado")
    country     = models.CharField(max_length=150, verbose_name="País")
    image       = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    latitude    = models.TextField(verbose_name="Latitude")
    longitude   = models.TextField(verbose_name="Longetude")
    
    
    def __str__(self):
        return self.name
    

