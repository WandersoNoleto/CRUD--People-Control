from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Feedback(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    comment = models.TextField(verbose_name="Comentário")
    score   = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Pontuação")
    date    = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    approved = models.BooleanField(default=True, verbose_name="Aprovado")

    def __str__(self):
        return self.user.username
    