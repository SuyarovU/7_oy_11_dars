from django.db import models


class Movie(models.Model):
    nom = models.CharField()
    janr = models.CharField(choices=[
        ('action', 'Action'),
        ('detectiv', 'Detectiv'),
        ('drama', 'Drama'),
        ('animation', 'Animation')
    ])
    yil = models.IntegerField()
    rejissor = models.CharField()
    
