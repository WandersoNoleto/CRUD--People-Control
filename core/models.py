from django.db import models

from feedback.models import Feedback
from location.models import Location
from tourist_resources.models import Resourse


class TourismSpot(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    approved  = models.BooleanField(default=False, verbose_name="Aprovado")
    resourses = models.ManyToManyField(Resourse, verbose_name="Recursos")
    feedbacks = models.ManyToManyField(Feedback, verbose_name="Avaliações")
    location  = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Localização")
    image     = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

