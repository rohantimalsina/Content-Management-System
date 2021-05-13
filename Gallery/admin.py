from django.contrib import admin

# Register your models here.
from .models import summer,campus,tour

admin.site.register(summer),
admin.site.register(campus),
admin.site.register(tour),