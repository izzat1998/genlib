from django.db import models


# Create your models here.
from GenLib import settings


class Book(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    genre = models.ManyToManyField('Genre', related_name='books', blank=True)
    file = models.FileField(upload_to='books', blank=True, null=True)
    author = models.ForeignKey('Author', related_name='books', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'book'

    @property
    def image_absolute_url(self):
        return "https://{0}{1}".format(settings.SERVER_NAME, self.image.url)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.name_ru


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name
