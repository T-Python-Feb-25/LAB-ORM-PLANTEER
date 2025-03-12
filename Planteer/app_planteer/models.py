from django.db import models

# Create your models here.

# 🏷️ نموذج الفئة لتحديد تصنيفات النباتات بشكل ديناميكي
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # ✅ الاسم يجب أن يكون فريدًا

    def __str__(self):
        return self.name
    
#/////////////////////

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    poster=models.ImageField(upload_to="images/",default="images/default.jpg")
    # يمكن إضافة المزيد من الحقول حسب الحاجة...
#//////////////////////////////////

    # ✅ **ربط النبات بفئة ديناميكية بدلًا من قائمة ثابتة**
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, help_text="Choose the category of the plant.")

    # ✅ **إضافة `is_edible` لتحديد ما إذا كان النبات صالحًا للأكل**
    is_edible = models.BooleanField(default=False, help_text="Check if the plant is edible.")

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100, verbose_name="full_name")
    content = models.TextField(verbose_name="comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")

    def __str__(self):
       return f"Comment by {self.full_name} on {self.plant.name}"
    



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)  # ✅ يتم تسجيل تاريخ الإرسال تلقائيًا

    def __str__(self):
        return f"Message from {self.full_name} - {self.subject}"