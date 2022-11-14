from django.shortcuts import render
from django.http import HttpRequest
from.models import New_Place as Place
from.models import Comment,Contact
from django.contrib.auth.models import User





#Home view

def home (request:HttpRequest):
    return render(request,'wijhaApp/home.html')

#------------------------------------------------------------------------


#add new place

def add_view (request:HttpRequest):
    user : User = request.user
    if request.method=="POST":
        new_place=Place(user=request.user ,place_name=request.POST["place_name"],city=request.POST["city"],content=request.POST["content"])
        new_place.save()

    return render(request,'wijhaApp/add_view.html')


#------------------------------------------------------------------------

#list views 

def list_places(request:HttpRequest):
    places=Place.objects.all()
    print(places)
    return render(request,'wijhaApp/views_place.html',{"place":places})


#------------------------------------------------------------------------
#add contact

def contact (request:HttpRequest):
    if request.method=="POST":
        new_contact=Contact(name=request.POST["name"],email=request.POST["email"],problem=request.POST["problem"])
        new_contact.save()
        print(new_contact)
    return render(request,'wijhaApp/contact.html')


#------------------------------------------------------------------------

def detail_of_place(request : HttpRequest, place_id : int):

    try:
        detail_of_place = Place.objects.get(id=place_id)
        #comments = Comment.objects.filter(post = post)
    except:
        return render(request ,"wijhaApp/home.html")

    return render(request, "wijhaApp/place_detail.html", {"place" : detail_of_place})





def list_commint(request:HttpRequest):
    pass


def control_view (request:HttpRequest):
    return render(request,'wijhaApp/control_view.html')





