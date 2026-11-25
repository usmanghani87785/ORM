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