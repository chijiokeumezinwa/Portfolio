from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    field = models.URLField(max_length = 200,  blank=True, default='')
    # image = models.FilePathField(upload_to="/projects/img")
    image = models.ImageField(blank=True, upload_to='images')