from django.db import models

# Create your models here.
class Course(models.Model):
	title=models.CharField(max_length=100)

class School(models.Model):
	name_of_school=models.CharField(max_length=100)
	name_of_degree=models.CharField(max_length=100)
	Month_Year_Start=models.CharField(max_length=50)
	Month_Year_End=models.CharField(max_length=50)

class Experience(models.Model):
	title=models.CharField(max_length=200)
	company=models.CharField(max_length=200)
	description=models.TextField()
	Month_Year_Start=models.CharField(max_length=50)
	Month_Year_End=models.CharField(max_length=50)