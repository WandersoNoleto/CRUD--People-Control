from django.db import models


class TourismSpot(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")

    def __str__(self):
        return self.name
    

