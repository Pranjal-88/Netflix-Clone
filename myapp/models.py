from django.db import models
from datetime import datetime

class Movie(models.Model):
    genres=[
        ('action','Action'),
        ('adventure','Adventure'),
        ('comedy','Comedy'),
        ('drama','Drama'),
        ('thriller','Thriller'),

    ]
    movie_name=models.CharField(max_length=200)
    description=models.CharField(max_length=100000)
    duration=models.PositiveIntegerField()
    genre=models.CharField(max_length=30,choices=genres)
    img_card=models.ImageField(upload_to='movie_cards')
    release_data=models.DateField(default=datetime.now)
    added_to_list=models.BooleanField(default=False)

    def __str__(self):
        return self.movie_name
