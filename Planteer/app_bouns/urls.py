from django.urls import path
from .views import add_comment

urlpatterns = [
    path('plants/<int:plant_id>/comment/', add_comment, name='add_comment'),
]