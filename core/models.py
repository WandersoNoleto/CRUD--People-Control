from django.db import models

from feedback.models import Feedback
from interested_points.models import Resourse
from location.models import Location


class TourismSpot(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    approved  = models.BooleanField(default=False, verbose_name="Aprovado")
    resourses = models.ManyToManyField(Resourse, verbose_name="Recursos")
    feedbacks = models.ManyToManyField(Feedback, verbose_name="Avaliações")
    location  = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Localização")

    def __str__(self):
        return self.name
    

