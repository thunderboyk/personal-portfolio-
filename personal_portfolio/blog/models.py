from django.db import models

# Create your models here.

# Create your models here.
class Blogs(models.Model):
		title = models.CharField(max_length=100)
		discription = models.CharField(max_length=250)
		