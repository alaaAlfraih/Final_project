from django.shortcuts import render
from django.http import HttpRequest
from.models import New_Place as Place




#Home view
def home (request:HttpRequest):
    return render(request,'wijhaApp/home.html')

#------------------------------------------------------------------------


#def register (request:HttpRequest):
    #return render(request,'wijhaApp/register.html')

#def login (request:HttpRequest):
    #return render(request,'wijhaApp/logIn.html')


#------------------------------------------------------------------------

#add new place

def add_view (request:HttpRequest):
    if request.method=="POST":
        new_place=Place( place_name=request.POST["place_name"],city=request.POST["city"],content=request.POST["content"])
        new_place.save()
        print(new_place)

    return render(request,'wijhaApp/add_view.html')


#------------------------------------------------------------------------

#list views 
def list_places(request:HttpRequest):
    places=Place.objects.all()
    print(places)
    return render(request,'wijhaApp/views_place.html',{"place":places})


#------------------------------------------------------------------------

def contact (request:HttpRequest):
    return render(request,'wijhaApp/contact.html')

def control_view (request:HttpRequest):
    return render(request,'wijhaApp/control_view.html')





