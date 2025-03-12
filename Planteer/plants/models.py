from django.db import models

# Create your models here.
class plant(models.Model):
    name=models.CharField(max_length=512)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/", default="image/روز.jpg")
    category=models.CharField(max_length=512)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)

class contact(models.Model):
    first_name=models.CharField(max_length=512)
    last_name=models.CharField(max_length=512)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
