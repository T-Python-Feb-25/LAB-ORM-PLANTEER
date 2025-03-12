from django.urls import path
from .views import add_comment

urlpatterns = [
    path('comment/', add_comment, name='add_comment'),
]