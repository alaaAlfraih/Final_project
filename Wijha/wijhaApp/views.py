from django.shortcuts import render
from django.http import HttpRequest




#Home view
def home (request:HttpRequest):
    return render(request,'wijhaApp/home.html')


def register (request:HttpRequest):
    return render(request,'wijhaApp/register.html')

def login (request:HttpRequest):
    return render(request,'wijhaApp/logIn.html')

def add_view (request:HttpRequest):
    return render(request,'wijhaApp/add_view.html')

def contact (request:HttpRequest):
    return render(request,'wijhaApp/contact.html')
def control_view (request:HttpRequest):
    return render(request,'wijhaApp/control_view.html')





