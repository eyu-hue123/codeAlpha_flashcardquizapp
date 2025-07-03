from django.contrib import admin
from .models import Menu, Table, Inventory, Order

admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Inventory)
admin.site.register(Order)