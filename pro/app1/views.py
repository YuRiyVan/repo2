from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , "app1/home.html")

def base(request):
    return render(request , "app1/base.html")

# Create your views here.
