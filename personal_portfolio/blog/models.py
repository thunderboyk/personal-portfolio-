from django.db import models

# Create your models here.

# Create your models here.
class Blogs(models.Model):
		title = models.CharField(max_length=200)
		discription = models.TextField(max_length=1000)
		date = models.DateField()


		def __str__(self):
			return self.title