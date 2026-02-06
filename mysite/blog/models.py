from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspelers(models.Model):
    naam_voetballer = models.CharField(max_length=200)
    actuele_voetbalclub = models.CharField(max_length=200)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.save()
    
    def __str__(self):
        return self.naam_voetballer