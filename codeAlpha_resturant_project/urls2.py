from django.urls import include, path
from rest_framework import routers
from .views import MenuViewSet, TableViewSet, InventoryViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'tables', TableViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]