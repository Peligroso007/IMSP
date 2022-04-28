from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404


def Logout(request):
    logout(request)
    return redirect('home')