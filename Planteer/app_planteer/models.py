from django.db import models

# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # يمكن إضافة المزيد من الحقول حسب الحاجة...

    def __str__(self):
        return self.name

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100, verbose_name="full_name")
    content = models.TextField(verbose_name="comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")

    def __str__(self):
       return f"Comment by {self.full_name} on {self.plant.name}"