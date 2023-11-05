# Ex02 Django ORM Web Application
## Date:18:10:23 

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
models.py
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
admin.py
from django.contrib import admin
from .models import Players,PlayersAdmin
admin.site.register(Players,PlayersAdmin)

# Register your models here.
```

## OUTPUT
![Alt text](<Screenshot 2023-10-18 092805.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
