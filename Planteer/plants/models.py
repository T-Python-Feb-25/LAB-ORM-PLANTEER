from django.db import models

# Create your models here.
class Plant(models.Model):
    class CategoryChoice(models.TextChoices):
        VEGETABLE = "Vegetable", "Vegetable"
        FRUIT = "Fruit", "Fruit"
        TREE = "Tree", "Tree"
    name=models.CharField(max_length=1024)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/")
    category=models.CharField(max_length=1024,choices=CategoryChoice.choices)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
class Comment(models.Model):
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=1024)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
