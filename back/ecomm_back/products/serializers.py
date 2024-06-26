from rest_framework import serializers
from .models import Product, Category, Order, OrderItem, Task

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many = True, read_only = True)

    class Meta:
        model = Order
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'