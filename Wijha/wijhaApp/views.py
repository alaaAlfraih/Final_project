from django.shortcuts import render
from django.http import HttpRequest




#Home view
def home (request:HttpRequest):
    return render(request,'wijhaApp/home.html')


# Create your views here.
