from django.db import models


# Create your models here.
class Movie(models.Model):

    name = models.CharField(max_length=250)
    dis = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
