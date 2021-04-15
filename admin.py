from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Course


# Register your models here.
admin.site.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
	list_display = ['id','title','course_structure','credit_distribution']


#customizing admin header
admin.site.site_header = "Herald College Kathmandu"
admin.site.site_title = "HCK"
admin.site.index_title = "Admin DashBoard"

#Unregistered group
admin.site.unregister(Group)
