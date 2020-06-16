from django.db import models

# Create your models here

class material(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000)
    url = models.URLField(blank=True)


class People(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    topic_1 = models.CharField(max_length=1000, blank=True)
    topic_2 = models.CharField(max_length=1000, blank=True)
    topic_3 = models.CharField(max_length=1000, blank=True)
    url_1 = models.URLField(blank=True)
    url_2 = models.URLField(blank=True)

class Course(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    topic_1 = models.CharField(max_length=1000, blank=True)
    topic_2 = models.CharField(max_length=1000, blank=True)
    topic_3 = models.CharField(max_length=1000, blank=True)
    url_1 = models.URLField(blank=True)

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    text = models.TextField(max_length=10000)

    #This function is to make the name of the object whatever you want like the title
    #It needs to be indented
    #it doesn't involve the database itself, so it doesn't need a migration
    def __str__(self):
        return self.title
