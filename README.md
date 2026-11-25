# Ex02 Django ORM Web Application

## Date: 25.11.2026

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 cars

## PROGRAM

```
model.py

from django.db import models
class Car(models.Model):
    car_id = models.CharField(max_length=20, primary_key=True, help_text="Car ID")
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.brand + " " + self.model



from django.db import models
from django.contrib import admin


class Car(models.Model):

    car_id = models.CharField(
        max_length=20,
        primary_key=True,
        help_text="Car ID"
    )

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.IntegerField()

    price = models.IntegerField()

    fuel_type = models.CharField(max_length=50)

    quantity = models.IntegerField()

    color = models.CharField(max_length=50)

    def __str__(self):
        return self.brand + " " + self.model


class CarAdmin(admin.ModelAdmin):

    list_display = (
        'car_id',
        'brand',
        'model',
        'year',
        'price',
        'fuel_type',
        'quantity',
        'color'
    )

 admin.py

from django.contrib import admin
from .models import Car,CarAdmin

admin.site.register(Car, CarAdmin)
```

## OUTPUT

![alt text](<Screenshot 2026-11-25 225912.png>)

## RESULT
Thus the program for creating car inventory database using ORM has been executed successfully