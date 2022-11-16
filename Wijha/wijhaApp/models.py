from django.db import models
from django.contrib.auth.models import User

class New_Place(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    place_name=models.CharField(max_length=1024)
    city=models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now=True)
    content=models.TextField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.place_name}, {self.created_at}"


class Comment(models.Model):

    new_place = models.ForeignKey(New_Place, on_delete = models.CASCADE)
    user_name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.new_place.place_name}, {self.content}"

class Contact(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    problem=models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}"
# Create your models here.
