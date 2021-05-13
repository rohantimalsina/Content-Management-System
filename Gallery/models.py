from django.db import models

# Create your models here.
class summer(models.Model):
	title = models.CharField(max_length = 200)
	image = models.FileField(upload_to='galleries',blank=True)

	def __str_(self):
		return self.title

	class Meta:
		verbose_name= "summer"
		verbose_name_plural="summer"

class campus(models.Model):
	title = models.CharField(max_length = 200)
	image = models.FileField(upload_to='galleries',blank=True)

	def __str_(self):
		return self.title

	class Meta:
		verbose_name= "campus"
		verbose_name_plural="campus"

class tour(models.Model):
	title = models.CharField(max_length = 200)
	image = models.FileField(upload_to='galleries',blank=True)

	def __str_(self):
		return self.title

	class Meta:
		verbose_name= "tour"
		verbose_name_plural="tour"



