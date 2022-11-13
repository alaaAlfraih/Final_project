from django.db import models

class New_Place(models.Model):
    place_name=models.CharField(max_length=1024)
    city=models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now=True)
    content=models.TextField()
# Create your models here.
