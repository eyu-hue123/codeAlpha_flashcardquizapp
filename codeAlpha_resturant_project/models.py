from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def str(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def str(self):
        return f"Table {self.number}"

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def str(self):
        return self.item_name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Order {self.id} - Table {self.table.number}"