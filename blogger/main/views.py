from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post
from .forms import PostForm
from django.db.models import Q
from datetime import datetime


def home(request):
    # تحديد تاريخ 9 مارس
    date_threshold = datetime(2025, 3, 9)

    # جلب البوستات التي نشرت بعد تاريخ 9 مارس
    posts = Post.objects.filter(published_at__gt=date_threshold).order_by('-published_at')

    return render(request, 'main/home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = PostForm()
    return render(request, 'main/add_post.html', {'form': form})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # إذا كان هناك طلب حذف
    if request.method == 'POST' and 'delete' in request.POST:
        post.delete()
        return redirect('main:home')  # العودة إلى الصفحة الرئيسية بعد الحذف

    return render(request, 'main/post_detail.html', {'post': post})

# دالة التعديل
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # تأكد من أن المستخدم هو من أنشأ البوست
    if request.user != post.user:
        return redirect('main:home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'main/update_post.html', {'form': form, 'post': post})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')




def search_view(request: HttpRequest):
    query = request.GET.get("search", "").strip()

    if query:
        posts = Post.objects.filter(title__icontains=query)

        # إذا لم يتم العثور على نتائج، ابحث عن المشاركات التي تحتوي على كلمات مشابهة
        if not posts.exists():
            words = query.split()
            query_conditions = Q()
            for word in words:
                query_conditions |= Q(title__icontains=word)
            posts = Post.objects.filter(query_conditions).distinct()

    else:
        posts = Post.objects.all()  # في حالة البحث الفارغ، يمكن عرض كل المشاركات أو لا شيء.

    return render(request, "main/search.html", {"posts": posts, "search_query": query})
