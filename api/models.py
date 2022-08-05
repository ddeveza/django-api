#this is where you schema or model is setup up

from django.db import models

class Api(models.Model):
    name=models.CharField(max_length=200) #name field 
    description = models.CharField(max_length=500) #descrption field

    def __str__(self): # to rename the title in admin page of django framework
        return self.name