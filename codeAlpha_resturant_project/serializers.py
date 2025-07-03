from rest_framework import serializers
from .models import Menu, Table, Inventory, Order

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = 'all'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = 'all'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = 'all'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = 'all'