from django.urls import path
from. import views

app_name="wijhaApp"

urlpatterns = [
    path('home/',views.home,name="home")
]