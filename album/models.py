from django.db import models
from musician.models import MusicianModel

# Create your models here.

class AlbumModel(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
