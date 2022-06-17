from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import  task


class taskSerializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

    
        