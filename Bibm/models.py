from django.db import models

# Create your models here.

#Model for courses
class bibm_Year_1(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bibm_Year_1"
		verbose_name_plural="bibm_Year_1"

class bibm_Year_2(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bibm_Year_1"
		verbose_name_plural="bibm_Year_1"

class bibm_Year_3(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bibm_Year_1"
		verbose_name_plural="bibm_Year_1"

class bibm_Year_4(models.Model):
	course_code = models.CharField(max_length = 150)
	course_name = models.TextField()

	def _str_(self):
		return self.course_code

	class Meta:
		verbose_name= "bibm_Year_1"
		verbose_name_plural="bibm_Year_1"

	

