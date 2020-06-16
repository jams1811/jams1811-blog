from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


#This function is to make the name of the object whatever you want like the title
#It needs to be indented

    def __str__(self):
        return self.title
