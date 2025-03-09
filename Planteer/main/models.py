from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)    