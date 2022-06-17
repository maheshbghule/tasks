from django.contrib import admin
from . models import task

# class task(admin.modeladmin):
#     list_display=["name",]
# Register your models here.
admin.site.register(task)
