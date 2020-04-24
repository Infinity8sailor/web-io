# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request,'interface/root.html')

def home(request):
    return render(request,'interface/home.html')

def about(request):
    return render(request,'interface/about.html')    

def me(request):
    return render(request,'extra/images/me.jpg')        
        