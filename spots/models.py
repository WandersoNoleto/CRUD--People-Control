from django.db import models


class TourismSpot(models.Model):
    name        = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    resourses   = models.TextField(verbose_name="Recursos")
    neighborhood= models.CharField(max_length=150, verbose_name="Bairro", null=True, blank=True)
    city        = models.CharField(max_length=150, verbose_name="Cidade", null=True, blank=True)
    state       = models.CharField(max_length=150, verbose_name="Estado", null=True, blank=True)
    country     = models.CharField(max_length=150, verbose_name="País", null=True, blank=True)
    image       = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

