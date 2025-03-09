from django.db import models

# Create your models here.

class Plant(models.Model):

  class CategoryChoices(models.TextChoices):
    INDOOR = "Indoor", "Indoor Plants"
    OUTDOOR = "Outdoor", "Outdoor Plants"
    FLOWERING = "Flowering", "Flowering Plants"
    SUCCULENTS = "Succulents", "Succulents & Cacti"
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