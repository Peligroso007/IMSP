from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inmsp.models.sales import Sales
from django.db.models import Sum
from inmsp.models.payment import Payment
from inmsp.models.product import Product
# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def dashboard(request):
    total_amount = Sales.objects.aggregate(Sum('grand_total'))
    todays_sale = Payment.objects.all().count()
    total_products = Product.objects.all().count()
    return render(request, 'dashboard/dashboards.html',{'total_amount': total_amount['grand_total__sum'], 'todays_sale': todays_sale, 'total_products': total_products})
