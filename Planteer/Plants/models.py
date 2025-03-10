from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices= [
        ('Tree', 'Tree'),
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Flower', 'Flower'),
        ('Herb', 'Herb'),
    ]
    )

    about = models.TextField()
    used_for = models.CharField(max_length=255)
    is_edible = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    

