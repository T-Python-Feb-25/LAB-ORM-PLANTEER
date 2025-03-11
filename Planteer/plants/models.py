from django.db import models

# Create your models here.


class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('Flowers', 'Flowers'),
        ('Trees', 'Trees'),
        ('Shrubs', 'Shrubs'),
        ('Herbs', 'Herbs'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    created_at = models.DateTimeField(auto_now_add=True)
    related_plants = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.full_name} on {self.plant.name}"
