from django.db import models

# Create your models here.
class Plants(models.Model):
  class CategoryChoices(models.TextChoices):
    FLOWER = 'flower', 'Flower'
    TREE = 'tree', 'Tree'
    VEGETABLE = 'vegetable', 'Vegetable'
    FRUIT = 'fruit', ' Fruit'

  name = models.CharField(max_length=100)
  about = models.TextField()
  used_for = models.TextField()
  image = models.ImageField(upload_to='images/', default="images/default.jpg")
  category = models.CharField(max_length=250, choices=CategoryChoices.choices)
  is_edible = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=250)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)


