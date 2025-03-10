from django.db import models

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('Tree', 'Tree'),
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Herb', 'Herb'),
        ('Flower', 'Flower'),
    ]

    name = models.CharField(max_length=255)
    about = models.TextField()  
    used_for = models.TextField()
    image = models.ImageField(upload_to='plants/')  
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  
    is_edible = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="comments")  
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.full_name} on {self.plant.name}"    

# Create your models here.
