from django.db import models

# Create your models here.

class Plant(models.Model):

  class CategoryChoices(models.TextChoices):
    FLOWERING = "Flowering", "Flowering Plants"
    HERBS = "Herbs", "Herbs & Medicinal Plants"
    TREES = "Trees", "Trees & Shrubs"
    FRUIT = "Fruit", "Fruit Plants & Trees"
    VEGETABLES = "Vegetables", "Vegetable Plants"


  name = models.CharField(max_length=1024)
  about = models.TextField()
  user_for = models.TextField()
  image = models.ImageField(upload_to="images/", default="images/default.png")
  category = models.CharField(max_length= 20 ,choices=CategoryChoices.choices)
  is_edible = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add= True)

class Comment(models.Model):
  plant = models.ForeignKey(Plant, on_delete= models.CASCADE)
  full_name = models.CharField(max_length= 512)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

class Conatct(models.Model):
  first_name = models.CharField(max_length=512)
  last_name = models.CharField(max_length=512)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
