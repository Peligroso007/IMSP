from django.urls import path
from inmsp.views import admin_controller, staff_controller, inventory_controller, stock_controller, payment_controller, suppliers_controller, product_controller
from inmsp.views.frontend import logout_controller

urlpatterns = [
    path('logout', logout_controller.Logout, name='logout'),
    path('admin/dashboard/', admin_controller.dashboard, name='admin'),
    path('admin/dashboard/staff', staff_controller.Staff, name='staff'),
    path('admin/dashboard/inventory', inventory_controller.Inventory, name='inventory'),
    path('admin/dashboard/stock', stock_controller.stock, name='stock'),
    path('admin/dashboard/payment', payment_controller.Payment, name='payment'),
    path('admin/dashboard/suppliers', suppliers_controller.suppliers, name='suppliers'),


    path('admin/dashboard/delete-user/<int:staff_id>', staff_controller.Delete_User, name='delete_user'),
    path('admin/dashboard/edit-user/<int:staff_id>', staff_controller.Edit_User, name='edit_user'),
    path('admin/dashboard/add-user/', staff_controller.Add_User, name='add_user'),


    path('admin/dashboard/add-product/', product_controller.add_product, name='add_product'),
    path('admin/dashboard/delete-product/<int:product_id>', product_controller.Delete_Product, name='delete_product'),
    path('admin/dashboard/edit-product/<int:product_id>', product_controller.edit_product, name='edit_product'),


    path('admin/dashboard/add-suppliers/', suppliers_controller.add_suppliers, name='add_suppliers'),
    path('admin/dashboard/edit-suppliers/<int:suppliers_id>', suppliers_controller.edit_suppliers, name='edit_suppliers'),
    path('admin/dashboard/delete-suppliers/<int:suppliers_id>', suppliers_controller.delete_supplier, name='delete_suppliers'),


    path('admin/dashboard/add-stock/', stock_controller.add_stock, name='add_stock'),
    path('admin/dashboard/add-quantity/<int:stock_id>', stock_controller.add_quantity, name='add_quantity'),






]