from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_shopkeeper = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    location_lat = models.FloatField(default=0)
    location_lng = models.FloatField(default=0)


class Storekeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image_url = models.CharField(max_length=2083)
    stock = models.IntegerField()
    price = models.FloatField()
    department = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    address = models.CharField(max_length=300)
    emirate = models.CharField(max_length=50)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=20)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    item_price = models.FloatField()