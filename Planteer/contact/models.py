from django.db import models

# Create your models here.
class Contact(models.Model):
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)