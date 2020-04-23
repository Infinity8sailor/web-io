# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> interface is getting started ......</h1>')

def home(request):
    return render(request,'extra/home_temp.html')
        