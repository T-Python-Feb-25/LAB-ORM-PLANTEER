from django.db import models

from app_main.models import Plant
# Create your models here.


class Comment(models.Model):
    plant = models.ForeignKey(Plant, related_name='comments', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

