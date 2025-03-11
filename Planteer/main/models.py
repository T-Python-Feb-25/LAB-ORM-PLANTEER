from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=255)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the date and time when a plant is created

    def __str__(self):
        return self.name
