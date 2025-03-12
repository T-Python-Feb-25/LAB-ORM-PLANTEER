from django.db import models

# Create your models here.


class Plant(models.Model):
    title  = models.CharField(max_length=2048)
    content  = models.TextField()
    types = models.CharField(max_length=2048)
    published_at  = models.DateTimeField(auto_now_add=True)