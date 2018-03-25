from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    director = models.ForeignKey(Person)
    actor = models.ManyToManyField(Person, through="Role", related_name="actors")
    year = models.IntegerField

    def __str__(self):
        return self.title

class Role(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.name