from django.db import models

# Create your models here.

class Plant(models.Model):

    name = models.CharField(max_length=2010)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField()
    categoy = models.CharField(max_length=2010)
    is_edible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=2010)


