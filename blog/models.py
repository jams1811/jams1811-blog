from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    #This function is to make the name of the object whatever you want like the title
    #It needs to be indented
    #it doesn't involve the database itself, so it doesn't need a migration
    def __str__(self):
        return self.title
