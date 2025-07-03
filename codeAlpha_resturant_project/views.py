from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Menu, Table, Inventory, Order
from .serializers import MenuSerializer, TableSerializer, InventorySerializer, OrderSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        table = self.get_object()
        if table.is_available:
            table.is_available = False
            table.save()
            return Response({'status': 'table reserved'})
        else:
            return Response({'status': 'table not available'}, status=400)

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer