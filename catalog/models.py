from django.db import models
from django.urls import reverse

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 50)
    rating = models.CharField(max_length = 2)

    def __str__(self):
        return self.name
class Cinema(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    movies = models.ManyToManyField(Movies, help_text='Select a movie')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie-detail', args = [str(self.id)])

class Auditorium(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    seats = models.IntegerField(max_length = 3)

class ShowTiming(models.Model):
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE())
    audi_id = models.ForeignKey(Auditorium, on_delete=models.SET_NULL())
    movie_id = models.ForeignKey(Movies, on_delete=models.SET_NULL())
    start_time = models.DateTimeField(null=False)
    price = models.FloatField(null=False)
    # seats_available =

class BookingData(models.Model):
    no_of_tkts = models.IntegerField(null = False)
    total_price = models.FloatField(null = False)
    show_details = models.ForeignKey(ShowTiming, on_delete=models.CASCADE())






