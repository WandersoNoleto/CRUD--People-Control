from django.db import models


class Resourse(models.Model):
    name            = models.CharField(max_length=150, verbose_name="Nome")
    description     = models.TextField(verbose_name="Descrição")
    operating_hours = models.TextField(verbose_name="Horário de funcionamento")
    age_required    = models.IntegerField(verbose_name="Idade Mínima", default=0)

    def __str__(self):
        return self.name
