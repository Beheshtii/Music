from django.db import models
from django.core.validators import FileExtensionValidator


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    family = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    avatar = models.ImageField(upload_to='images/artist/', verbose_name='آواتار')

    class Meta:
        db_table = 'Artist'
        verbose_name = 'خواننده'
        verbose_name_plural = 'خوانندگان'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')

    class Meta:
        db_table = 'Category'
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')

    class Meta:
        db_table = 'Country'
        verbose_name = 'کشور'
        verbose_name_plural = 'کشورها'

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    year = models.DateField(verbose_name='تاریخ')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='خواننده')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='کشور')
    photo = models.ImageField(upload_to='images/music/', verbose_name='تصویر')
    file = models.FileField(upload_to='music/files/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'flac', 'ogg'])],
        verbose_name='فایل موزیک',
    )

    class Meta:
        db_table = 'Music'
        verbose_name = 'آهنگ'
        verbose_name_plural = 'آهنگ ها'

    def __str__(self):
        return f"{self.title} - {self.artist.name}"
