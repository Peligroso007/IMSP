from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inmsp.models.suppliers import Suppliers
from inmsp.models.product import Product
from inmsp.models.stock import Stock
# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def stock(request):
    suppliers = Suppliers.objects.all()
    products = Product.objects.all()
    stocks = Stock.objects.all()

    return render(request, 'stock/stock.html', {'suppliers': suppliers, 'products': products, 'stocks': stocks})


def add_stock(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_name')
        suppliers_id = request.POST.get('suppliers_name')
        quantity_imported = request.POST.get('quantity_imported')

        quantity_sold = 0
        quantity_remaining = int(quantity_imported) - int(quantity_sold)

        supplier = Suppliers.objects.get(id=suppliers_id)

        stock = Stock.objects.create(suppliers=supplier, quantity_imported= quantity_imported, quantity_remaining=quantity_remaining, quantity_sold=quantity_sold)
        stock.save()

        product = Product.objects.get(id=product_id)
        product.product_stock = stock
        product.save()

        return redirect('stock')

    return redirect('stock')


def add_quantity(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    if request.method == 'POST':
        quantity_imported = request.POST.get('quantity_imported')

        stock.quantity_imported += int(quantity_imported)
        stock.quantity_remaining = int(stock.quantity_imported) - int(stock.quantity_sold)
        stock.save()

        return redirect('stock')

    return redirect('stock')        