from django.db import models
from datetime import datetime, date
from django.utils import timezone

# Create your models here.
class newevent(models.Model):
	title = models.CharField(max_length = 200)
	date_and_time = models.DateTimeField()
	venue = models.CharField(max_length = 200)
	description = models.TextField(max_length = 300)

	def __str_(self):
		return self.title

	class Meta:
		verbose_name= "newevents"
		verbose_name_plural="newevents"