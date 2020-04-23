# interface/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'interface/index.html', context=None)