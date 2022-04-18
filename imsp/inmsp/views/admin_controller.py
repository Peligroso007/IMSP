from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def dashboard(request):
    return render(request, 'admin/dashboard.html')