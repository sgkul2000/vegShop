from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Vegitable(models.Model):
    id = models.AutoField(primary_key=True)
    WEIGHT_CHOICES = [
        ("1KG","one kilogram"),
        ("0.5KG","half kilogram"),
        ("0.25KG","quarterkilogram"),
    ]
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pricePer = models.CharField(max_length=10, choices=WEIGHT_CHOICES)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    orderDate = models.DateField(default=datetime.date.today)
    estimatedDelivery = models.DateField()
    amount = models.IntegerField()
    items = models.ManyToManyField(Vegitable, blank=True, related_name='vegitables')

class Users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    orders=models.ManyToManyField(Order, blank=True, related_name='orders')
