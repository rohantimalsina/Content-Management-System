from django.db import models

# Create your models here.

#Model for courses
class bit_Year_1(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bit_Year_1"
		verbose_name_plural="bit_Year_1"


	
class bit_Year_2(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bit_Year_2"
		verbose_name_plural="bit_Year_2"
	

class bit_Year_3(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bit_Year_3"
		verbose_name_plural="bit_Year_3"

	
