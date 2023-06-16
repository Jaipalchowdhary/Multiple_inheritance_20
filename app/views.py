from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def regi(request):
    return render(request,'regi.html')

def login(request):
    return render(request,'login.html')
    