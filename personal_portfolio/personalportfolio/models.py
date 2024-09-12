from django.db import models

# Create your models here.
class Project(models.Model):
		title = models.CharField(max_length=100)
		discription = models.CharField(max_length=1000)
		image = models.ImageField(upload_to='personalportfolio/image/')
		url= models.URLField(blank=True)


		def __str__(self):
			return self.title
			# for showing the title of the projects on the admin page 

		

    #not nessary for clicking is blank 