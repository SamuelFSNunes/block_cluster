from django.db import models

class MoviesModel(models.Model):
  CHOICES = {
        "L": "Livre",
        "10": "10 anos",
        "12": "12 anos",
        "14": "14 anos",
        "16": "16 anos",
        "18": "18 anos",
    }
  movie_id = models.IntegerField(primary_key=True,null=False, blank=False)
  title = models.CharField(max_length=100, null=False, blank=False)
  realease_year = models.DateField(null=False, blank=False)
  synopsis = models.TextField(null=True, blank=True)
  rating = models.FloatField(null=False, blank=False)
  duration = models.IntegerField(null=False, blank=False)
  age_rating = models.CharField(choices=CHOICES)
  production_company = models.CharField(null=False, blank=False)

  