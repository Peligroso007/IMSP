from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from inmsp.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout





# def Login(request):
#     return render(request, 'login/login.html')


def Login(request):
    username = request.user.username
    user_obj = User.objects.filter(username=username).first()
    profile_obj = Profile.objects.filter(user=user_obj).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, 'User not found.')
            return render(request, 'login/login.html')

        profile_obj = Profile.objects.filter(user = user_obj).first()
        # if not profile_obj.is_verified:
        #     messages.error(request, 'Account is not verified check your email.')
        #     return render(request, 'login/login.html')

        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.error(request, 'Credentials are wrong please check your username and password.')
            return render(request, 'login/login.html')

        login(request, user)

        

    if request.user.is_authenticated:
        return redirect('admin')


    return render(request, 'login/login.html')