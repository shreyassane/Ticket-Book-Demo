from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    name = models.Charfield(max_length = 200)
    genre = models.Charfield(max_length = 50)
    rating = models.Charfield(max_length = 2)

    def __str__(self):
        return self.name , self.genre, self.rating
class Cinema(models.Model):
    name = models.Charfield(max_length = 100)
    city = models.Charfield(max_length = 100)
    state = models.Charfield(max_length = 100)
    movies = models.ManyToManyField(Movie, help_text='Select a movie')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie-detail', args = [str(self.id)])

class Auditorium(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, null=True)
    seats = models.IntegerField(max_length = 3)

