from django.contrib.auth.models import AbstractUser , Permission , Group
from django.db import models

class Farmer(AbstractUser):
  address = models.TextField(max_length=300)
  mobile = models.CharField(max_length=12)
  profile = models.ImageField(upload_to='images/profile/', null=True, blank=True)
  total_area = models.IntegerField()
  groups = models.ManyToManyField(Group, related_name='farmer_groups' , blank=True , null= True)
  user_permissions = models.ManyToManyField(Permission, related_name='farmer_user_permissions' , blank=True , null= True)
  
  class Meta:
    verbose_name = 'Farmer'
    
    
    
class Crop(models.Model):
  name = models.CharField(max_length=100)
  area = models.IntegerField()
  farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
  

class Expenditure(models.Model):
  farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
  amount = models.IntegerField()
  date = models.DateField()
  description = models.TextField(max_length=300)
  
class Treatment(models.Model):
  crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
  date = models.DateField()
  image = models.ImageField(upload_to='images/treatment/', null=True, blank=True)
  description = models.TextField(max_length=300)
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  image = models.ImageField(upload_to='images/product/', null=True, blank=True)
  description = models.TextField(max_length=300)
  
class Order(models.Model):
  farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  date = models.DateField()
              
          