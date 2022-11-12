from django.urls import path
from. import views

app_name="wijhaApp"

urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="logIn"),
    path('views',views.add_view,name="add_view"),
    path('contact/',views.contact,name="contact"),
    path('control/',views.control_view,name="control_view")
]