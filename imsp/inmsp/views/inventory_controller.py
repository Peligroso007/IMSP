from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inmsp.models.product import Product
# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def Inventory(request):
    product = Product.objects.all()
    
    return render(request, 'inventory/inventory.html', {'product': product})