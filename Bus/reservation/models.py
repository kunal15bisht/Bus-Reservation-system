from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 32, unique = True)
    email = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)

class Bus(models.Model):
    username = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    bus_number = models.CharField(max_length=20)
    bus_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=40)
    available_seats = models.PositiveIntegerField(default=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bus_status = models.CharField(max_length = 32)
    
    def __str__(self):
        return f"{self.bus_name} ({self.bus_number}): {self.source} to {self.destination}"

class Reservation(models.Model):    
    username = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateField()
    No_of_person = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bus_number = models.CharField(max_length=20)
    bus_name = models.CharField(max_length=100)
    time = models.TimeField()
    bus_status = models.CharField(max_length=32, default='Active')

