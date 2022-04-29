from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inmsp.models.suppliers import Suppliers
# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def suppliers(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'suppliers/suppliers.html', {'suppliers': suppliers})


def add_suppliers(request):
    if request.method == 'POST':
        suppliers_name = request.POST.get('suppliers_name')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        suppliers = Suppliers.objects.create(suppliers_name=suppliers_name, location=location, contact=contact, email=email)
        suppliers.save()

        redirect('suppliers')


    return redirect('suppliers')


def edit_suppliers(request, suppliers_id):
    supplier = Suppliers.objects.get(id=suppliers_id)
    if request.method == 'POST':
        suppliers_name = request.POST.get('suppliers_name')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        supplier.suppliers_name = suppliers_name
        supplier.location = location
        supplier.contact = contact
        supplier.email = email
        supplier.save()

        return redirect('suppliers')


    return render(request, 'suppliers/edit.html', {'s': supplier})


def delete_supplier(request, suppliers_id):
    try:
        Suppliers.objects.get(pk=suppliers_id).delete()
        messages.success(request, "Suppliers is Successfully deleted.")
        return redirect('suppliers')
    except Exception as e:
        print(e)

    # messages.error(request, "Something went wrong.")
    return redirect('suppliers')