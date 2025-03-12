from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from app_main.models import Plant
from .forms import CommentForm

def add_comment(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.plant = plant
            comment.save()
            return redirect('plant_detail', plant_id=plant.id)  
    else:
        form = CommentForm()
    return render(request, 'app_bouns/add_comment.html', {'form': form, 'plant': plant})