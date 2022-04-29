from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inmsp.models.product import Product
from inmsp.models.payment import Payment
from inmsp.models.sales import Sales
from django.db.models import Sum

def Checkout(request):
    product = Product.objects.all()
    payments = Payment.objects.filter(now=True)

    grand_total = payments.aggregate(Sum("total_amount"))
    
    return render(request, 'checkout/checkout.html', {'product': product, 'payments': payments, 'grand_total': grand_total['total_amount__sum']})


def add_payment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        
        product = Product.objects.get(id=product_id)

        total = int(quantity) * int(product.product_marked_price)

        payment = Payment.objects.create(product=product, quantity=quantity, price=product.product_marked_price, total_amount=total)
        payment.save()

        return redirect('checkout')




    return redirect('checkout')


def add_sales(request):
    if request.method == 'POST':
        grand_total = request.POST.get('grand_total')

        sales = Sales.objects.create(grand_total=grand_total)
        sales.save()

        payments = Payment.objects.filter(now=True)
        Payment.objects.filter(now=True).update(sales=sales)
        payments.update(now=False)
        

        
        return redirect('checkout')




    return redirect('checkout')