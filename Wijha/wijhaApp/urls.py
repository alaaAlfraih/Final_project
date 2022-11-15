from django.urls import path
from. import views

app_name="wijhaApp"

urlpatterns = [
    path('home/',views.home,name="home"),
    path('views',views.add_view,name="add_view"),
    path('contact/',views.contact,name="contact"),
    path('control/',views.control_view,name="control_view"),
    path('places',views.list_places,name="list_places"),
    path('place/detail/<place_id>',views.detail_of_place,name="detail"),
    path('detail/manager/<place_id>',views.detail_of_place_manager,name="detail_manager")

    #path('commint',views,name="commint")
]