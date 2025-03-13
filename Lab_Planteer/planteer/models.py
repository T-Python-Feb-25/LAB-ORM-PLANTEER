from django.db import models

# Create your models here.


class Plant(models.Model):
    title  = models.CharField(max_length=2048)
    content  = models.TextField()
    types = models.CharField(max_length=2048, null=True)
    published_at  = models.DateTimeField(auto_now_add=True)
    plant_image = models.ImageField(upload_to="images/", default="images/default.jpeg")