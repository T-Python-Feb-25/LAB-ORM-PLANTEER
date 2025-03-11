from django.db import models

# Create your models here.

class Plants(models.Model):

    class CategoryChoices(models.TextChoices):
        ANNUALS = "Annuals" , "Annual"
        HERBS = "Herbs" , "Herb"
        SHRUBS = "Shrubs" , "Shrub"
        TREES = "Trees" , "Tree"
        FRUIT = "Fruits" , "Fruit"
        VEGETABLES = "Vegetables" , "Vegetable"



    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="image/")
    category = models.CharField(choices=CategoryChoices.choices,max_length=1024)
    is_edible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    plant = models.ForeignKey(Plants,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)