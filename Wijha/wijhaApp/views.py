from django.shortcuts import render,redirect
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

    if not (user.is_authenticated):
        return redirect("users:logIn")
    if request.method=="POST":
        new_place=Place(user=request.user ,place_name=request.POST["place_name"],city=request.POST["city"],content=request.POST["content"],image=request.FILES["image"])
        new_place.save()

    return render(request,'wijhaApp/add_view.html')


#------------------------------------------------------------------------

#list views 

def list_places(request:HttpRequest):
    if "search" in request.GET:
        places=Place.objects.filter(place_name__contains=request.GET["search"],is_approved=True)

    else:
        places=Place.objects.filter(is_approved=True)

    return render(request,'wijhaApp/views_place.html',{"place":places})


#------------------------------------------------------------------------
#add contact

def contact (request:HttpRequest):
    if request.method=="POST":
        new_contact=Contact(name=request.POST["name"],email=request.POST["email"],problem=request.POST["problem"])
        new_contact.save()
    return render(request,'wijhaApp/contact.html')


#------------------------------------------------------------------------
#add commint

def add_commint(request : HttpRequest, place_id : int):
    palce=Place.objects.get(id=place_id)
    if request.method=="POST":
        new_commint=Comment(content=request.POST["content"])
        new_commint.save()

    return render(request,'wijhaApp/add_commint.html',palce.id)



#------------------------------------------------------------------------
#print detail of place
def detail_of_place(request : HttpRequest, place_id : int):

    try:
        detail_of_place = Place.objects.get(id=place_id)
        comments = Comment.objects.filter( new_place = detail_of_place)
        print(comments)
    except:
        return render(request ,"wijhaApp/home.html")

    return render(request, "wijhaApp/place_detail.html", {"place" : detail_of_place,"commint":comments})


#------------------------------------------------------------------------
#print detail of place for manager


def detail_of_place_manager(request : HttpRequest, place_id : int):
    try:
        detail_of_place = Place.objects.get(id=place_id)
    except:
        return render(request ,"wijhaApp/home.html")

    place=Place.objects.get(id=place_id)
    if request.method=="POST":
        place.is_approved=request.POST["is_approved"]
        place.save()
        return redirect("wijhaApp:control_view")
    return render(request, "wijhaApp/place_detail_manager.html", {"place_approv" : place,"place":detail_of_place})

    #return render(request, "wijhaApp/place_detail_manager.html", {"place" : detail_of_place})



#------------------------------------------------------------------------

def list_commint(request:HttpRequest):
    pass

#------------------------------------------------------------------------
#manager 
def control_view (request:HttpRequest):
    user : User = request.user
    if not (user.is_authenticated and user.has_perm("wijhaApp.control_view")):
       return redirect("users:logIn")
    places=Place.objects.all()

    return render(request,'wijhaApp/control_view.html',{"place":places})


#------------------------------------------------------------------------

#is_approved  
def manager_agree (request:HttpRequest,place_id):
    place=Place.objects.get(id=place_id)
    if request.method=="POST":
        place.is_approved=request.POST["is_approved"]
        place.save()
        return redirect("wijhaApp:control_view")
    return render(request, "wijhaApp/place_detail_manager.html", {"place" : place})
    




