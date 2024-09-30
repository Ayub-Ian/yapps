from django.db import models
from core.models import Restaurant

# Create your models here.
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=50)

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)
    order_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item_id = models.IntegerField()  # Replace with a MenuItem model reference if needed
    quantity = models.IntegerField()
    customizations = models.TextField(null=True, blank=True)

