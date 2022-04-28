from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from inmsp.models.profile import Profile
import uuid
from decouple import config
from django.contrib import messages
from django.core.mail import send_mail


# from inmsp.templatetags.role_check import is_staff_or_admin



# @login_required()
# @user_passes_test(is_staff_or_admin)
def Staff(request):
    staffs = User.objects.all()
    return render(request, 'staff/staff.html', {'staffs': staffs})


@login_required()
def Add_User(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        name = request.POST.get('first_name') +" "+ request.POST.get('last_name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        role = request.POST.get('role')
        try:
            if User.objects.filter(username = username).first():
                messages.error(request, 'Username is taken.')
                return redirect('staff')

            if User.objects.filter(email = email).first():
                messages.error(request, 'Email is already in use by a user.')
                return redirect('staff')
            user_obj = User.objects.create(username = username, email = email, first_name = first_name, last_name = last_name)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())

            profile_obj = Profile.objects.create(user = user_obj, name = name, phone = phone, gender = gender, role = role, address = address, auth_token= auth_token)
            profile_obj.save()
            send_verification_mail(email,auth_token,username)

            return  redirect('staff')
        except Exception as e:
            print(e)

    return redirect('staff')



def send_verification_mail(email, token, username):
    subject = 'Your account need to be verified'
    message = f'Hi {username} please click on the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = config('EMAIL_HOST_USER')
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)









def Delete_User(request, staff_id):
    try:
        # employee = User.objects.filter(pk=staff_id).first()
        User.objects.get(pk=staff_id).delete()
        messages.success(request, "Employee is Successfully deleted.")
        return redirect('staff')
    except Exception as e:
        print(e)

    # messages.error(request, "Something went wrong.")
    return redirect('staff')

def Edit_User(request, staff_id):
    staff = User.objects.get(id=staff_id)
    # profile = Profile.objects.get(user=staff)
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        name = request.POST.get('first_name') +" "+ request.POST.get('last_name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        role = request.POST.get('role')

        try:
            staff.username = username
            staff.first_name = first_name
            staff.last_name = last_name
            staff.set_password(password)
            staff.email = email
            staff.save()
            
            staff.profile.name = name
            staff.profile.phone = phone
            staff.profile.gender = gender
            staff.profile.address = address
            staff.profile.role = role
            staff.profile.save()

            return  redirect('staff')
        except Exception as e:
            print(e)

        return redirect('staff')


    return render(request, 'staff/edit.html', {"staff": staff})



    