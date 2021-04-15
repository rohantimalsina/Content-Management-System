from django.db import models

# Create your models here.

#Model for courses
class Course(models.Model):
	title = models.CharField(max_length = 150)
	course_structure = models.TextField()
	credit_distribution = models.TextField()

	def __str__(self):
		return self.title
