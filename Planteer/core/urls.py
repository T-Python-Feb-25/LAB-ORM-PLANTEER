from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]



from django.urls import path
from .views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]



from django.urls import path
from .views import home, contact  
urlpatterns = [
    path('', home, name='home'),  
    path('contact/', contact, name='contact'),
]


