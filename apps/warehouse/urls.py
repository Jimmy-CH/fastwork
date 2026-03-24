from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'purchase-orders', views.PurchaseOrderViewSet)
router.register(r'inventories', views.InventoryViewSet)
router.register(r'transactions', views.InventoryTransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

