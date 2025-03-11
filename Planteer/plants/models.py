from django.db import models

# Create your models here.


class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        TREES = 'Trees', 'Trees'
        SHRUBS = 'Shrubs', 'Shrubs'
        GRASSES = 'Grasses', 'Grasses'
        VINES_CLIMBERS = 'Vines & Climbers', 'Vines & Climbers'
        HERBS = 'Herbs', 'Herbs'
        '''
        Herbs
        Trees
        Shrubs
        Vines & Climbers
        GrassesS
        '''
    name = models.CharField(max_length=512)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/') # ?
    category = models.CharField(max_length=512, choices=CategoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
class Comment(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    comment = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)