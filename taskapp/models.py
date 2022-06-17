from distutils.command.upload import upload
from statistics import mode
from tkinter import Image
from django.db import models
from django.forms import URLField


# Create your models here.


class task(models.Model):
    tasktype=models.CharField(max_length=50,null=False)
    Description=models.TextField(null=False)
    icon=models.URLField(max_length=600,null=False)
    # itext=models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.tasktype
         
    
