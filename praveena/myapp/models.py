from django.db import models
from django.contrib import admin
class Players(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    team_name=models.CharField(max_length=20)
    salary=models.IntegerField()
    weight=models.IntegerField()
    no_of_winning=models.IntegerField()
    email= models.EmailField()
    
class PlayersAdmin(admin.ModelAdmin):
    list_display=('name','age','team_name','salary','weight','no_of_winning','email')



# Create your models here.
