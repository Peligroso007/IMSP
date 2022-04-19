from django.urls import path
from inmsp.views import admin_controller, staff_controller, inventory_controller, stock_controller, payment_controller, suppliers_controller


urlpatterns = [
    path('admin/dashboard/', admin_controller.dashboard, name='admin'),
    path('admin/dashboard/staff', staff_controller.Staff, name='staff'),
    path('admin/dashboard/inventory', inventory_controller.Inventory, name='inventory'),
    path('admin/dashboard/stock', stock_controller.Stock, name='stock'),
    path('admin/dashboard/payment', payment_controller.Payment, name='payment'),
    path('admin/dashboard/suppliers', suppliers_controller.Suppliers, name='suppliers'),
]