from django.db import models
from django.contrib.auth.models import User

class ProductManager(models.Manager):
    def get_expensive_products(self):
        return self.get_queryset().filter(price__gt=100)
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    objects = ProductManager()

class Category(models.Model):
    name = models.CharField(max_length=100)

class OrderManager(models.Manager):
    def get_orders_by_user(self, user):
        return self.get_queryset().filter(user=user)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# e60f394ba5dd1a8d94cda1ce350ccae43e411a75 ali