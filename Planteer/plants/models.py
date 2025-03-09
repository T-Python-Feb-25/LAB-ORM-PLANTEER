from django.db import models

# Create your models here.

class Plant(models.Model):
    class PlantsCategory(models.TextChoices):
        INDOOR = 'indoor', 'Indoor Plants'
        OUTDOOR = 'outdoor', 'Outdoor Plants'
        FLOWERING = 'flowering', 'Flowering Plants'
        HERBS_MEDICINAL = 'herbs_medical', 'Herbs & Medicinal Plants'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(choices=PlantsCategory.choices,max_length=100)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name