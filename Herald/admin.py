from django.contrib import admin
from django.contrib.auth.models import Group




#customizing admin header
admin.site.site_header = "Herald College Kathmandu"
admin.site.site_title = "HCK"
admin.site.index_title = "Admin DashBoard"

#Unregistered group
admin.site.unregister(Group)
