from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/artist/')

    class Meta:
        db_table = 'Artist'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/music/')

    class Meta:
        db_table = 'Music'

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
