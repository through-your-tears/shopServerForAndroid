from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)


class Order(models.Model):
    date = models.DateField(auto_now=True)
    amount = models.IntegerField()
    address = models.CharField(max_length=256)
    payment_type = models.CharField(max_length=256)
    date_of_receipt = models.DateField()
    shelf_life = models.DateField()
    contact_number = models.CharField(max_length=12)
    contact_name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
