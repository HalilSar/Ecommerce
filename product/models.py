from django.db import models
from django.contrib.auth.models import User
import datetime
class Product(models.Model):
    
    productname= models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,)  
    def __str__(self):
        return self.productname
    class Meta:
        ordering = ['id']


class Category(models.Model):
    categoryname = models.CharField(max_length=100)
    def __str__(self):
        return self.categoryname


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)                           
    user = models.ForeignKey(User, on_delete=models.CASCADE)                              
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)