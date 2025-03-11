from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    is_edible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.full_name} on {self.plant.name}'
