from django.db import models
from core.models import Restaurant

# Create your models here.
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    active_status = models.BooleanField(default=True)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    availability_status = models.BooleanField(default=True)
    external_id = models.IntegerField(null=True)  # Link to POS system item ID


