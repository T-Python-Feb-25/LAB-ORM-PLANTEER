#from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from .models import Plant, Comment , Category ,ContactMessage
from .forms import PlantForm 
 # Create your views here.

# def home_page (request : HttpRequest):
  
#     return render(request, 'app_planteer/home_page.html')



def home_page(request: HttpRequest):
    # ✅ جلب 3 نباتات عشوائية لعرضها في الصفحة الرئيسية
    random_plants = Plant.objects.order_by('?')[:3]

    return render(request, 'app_planteer/home_page.html', {
        "random_plants": random_plants  # ✅ إرسال النباتات العشوائية إلى القالب
    })


def all_plants(request : HttpRequest):

   # planteer =Plant.objects.all()
   # return render(request, 'app_planteer/all_plants.html',{"planteer":planteer})

   
    # ✅ جلب جميع الفئات من قاعدة البيانات
    categories = Category.objects.all()

    # ✅ جلب جميع النباتات (بدون فلترة في البداية)
    planteer = Plant.objects.all()

    # 🏷️ الحصول على الفلاتر من الطلب (GET request)
    category_filter = request.GET.get('category', 'all')
    is_edible_filter = request.GET.get('is_edible', 'all')

    # ✅ تطبيق تصفية الفئات فقط إذا تم اختيار قيمة صحيحة
    if category_filter.isdigit() and Category.objects.filter(id=int(category_filter)).exists():
        planteer = planteer.filter(category__id=int(category_filter))

    # ✅ تصفية النباتات القابلة للأكل فقط إذا تم اختيار الفلتر
    if is_edible_filter == "true":
        planteer = planteer.filter(is_edible=True)

    return render(request, 'app_planteer/all_plants.html', {
        "planteer": planteer,  # ✅ إرسال قائمة النباتات المصفاة
        "categories": categories,  # ✅ إرسال جميع الفئات إلى القالب
        "selected_category": int(category_filter) if category_filter.isdigit() else None,
        "selected_is_edible": is_edible_filter,
    })




def add_plant(request : HttpRequest):

    if request.method=="POST":
       new_plant=Plant(name=request.POST["name"],description=request.POST["description"],poster=request.FILES["poster"])
       new_plant.save()
    #print(request.POST)
   
    return render(request, 'app_planteer/add_plant.html')




def search_plants(request: HttpRequest):
    query = request.GET.get("query", "").strip()  # ✅ التقاط مصطلح البحث وإزالة المسافات الزائدة
    plants = Plant.objects.filter(name__icontains=query) if query else []  # ✅ البحث عن النباتات التي تحتوي على الكلمة المدخلة


    # ✅ جلب نفس النباتات العشوائية التي تظهر في `home_page`
    random_plants = Plant.objects.order_by('?')[:3]

    return render(request, 'app_planteer/search_plants.html', {
        "plants": plants,
        "query": query,
        "random_plants": random_plants  # ✅ إرسال النباتات العشوائية إلى القالب
    })



def contact(request: HttpRequest):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # ✅ حفظ البيانات في قاعدة البيانات
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("app_planteer:contact_page_messages")  


    return render(request, 'app_planteer/contact.html')



def contact_page_messages(request: HttpRequest):
    # ✅ جلب جميع الرسائل المخزنة في قاعدة البيانات
    messages = ContactMessage.objects.all().order_by('-sent_at')  # ترتيب من الأحدث إلى الأقدم

    return render(request, 'app_planteer/contact_page_messages.html', {"messages": messages})



def plant_detail(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)  
    
    if request.method == "POST":
        new_comment = Comment(
            plant=plant,  # ✅ ربط التعليق بالنبات المحدد
            full_name=request.POST["full_name"],
            content=request.POST["comment"],
            created_at=timezone.now()
        )
        new_comment.save()
        return redirect('app_planteer:plant_detail', plant_id=plant.id)  # ✅ إعادة التوجيه بعد إضافة التعليق

    comments = plant.comments.all()  # ✅ جلب جميع التعليقات المرتبطة بالنبات
  
    # ✅ جلب النباتات المشابهة بناءً على نفس `category`، مع استثناء النبتة الحالية
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:4]  # عرض 4 نباتات مشابهة فقط

    return render(request, 'app_planteer/plant_detail.html', {
        "plant": plant,
        "comments": comments,
        "related_plants": related_plants  # ✅ إرسال النباتات المشابهة إلى `plant_detail.html`
    })



# 📝 View لتعديل النبتة
def plant_edit(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('app_planteer:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'app_planteer/plant_edit.html', {"form": form, "plant": plant})


def plant_delete(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)
    
    if request.method == "POST":
        plant.delete()
        return redirect('app_planteer:all_plants')  # 🔹 تأكد أن لديك قائمة للنباتات

    return render(request, 'app_planteer/plant_delete.html', {"plant": plant})