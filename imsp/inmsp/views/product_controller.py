from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inmsp.models.product import Product


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        catagory = request.POST.get('catagory')
        mark_price = request.POST.get('mark_price')
        discount = request.POST.get('discount')
        buying_price = request.POST.get('buying_price')
        expiry_date = request.POST.get('expiry_date')
        manufacture_date = request.POST.get('manufacture_date')

        product = Product.objects.create(product_name=name, product_type=catagory, product_marked_price=mark_price, product_discount=discount, product_buying_price=buying_price, product_experies=expiry_date, product_manufacture=manufacture_date)
        product.save()

        redirect('inventory')

    return redirect('inventory')


def Delete_Product(request, product_id):
    try:
        # employee = User.objects.filter(pk=staff_id).first()
        Product.objects.get(pk=product_id).delete()
        messages.success(request, "Product is Successfully deleted.")
        return redirect('inventory')
    except Exception as e:
        print(e)

    # messages.error(request, "Something went wrong.")
    return redirect('inventory')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        name = request.POST.get('product_name')
        catagory = request.POST.get('catagory')
        mark_price = request.POST.get('mark_price')
        discount = request.POST.get('discount')
        buying_price = request.POST.get('buying_price')
        expiry_date = request.POST.get('expiry_date')
        manufacture_date = request.POST.get('manufacture_date')

        product.product_name = name
        product.product_type = catagory
        product.product_marked_price = mark_price
        product.product_discount = discount
        product.product_buying_price = buying_price
        product.product_experies = expiry_date
        product.product_manufacture = manufacture_date
        product.save()

        return redirect('inventory')


    return render(request, 'inventory/edit.html', {'p':product})