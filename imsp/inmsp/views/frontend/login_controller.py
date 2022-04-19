from django.shortcuts import render, redirect, get_object_or_404



def Login(request):
    return render(request, 'login/login.html')