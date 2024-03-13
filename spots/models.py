from django.db import models


class TouristSpot(models.Model):
    name        = models.CharField(max_length=150)
    description = models.TextField()
    resources   = models.TextField()
    city        = models.CharField(max_length=150)
    state       = models.CharField(max_length=150)
    country     = models.CharField(max_length=150)
    image       = models.ImageField(upload_to='spots_image', null=True, blank=True)
    latitude    = models.FloatField()
    longitude   = models.FloatField()
        
    def __str__(self):
        return self.name
    

