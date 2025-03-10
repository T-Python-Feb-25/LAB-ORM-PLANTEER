
from django.urls import path
from . import views
app_name="main"
urlpatterns=[path("",views.home_view,name="home_view"),
              path("contact/us/",views.contact_us_view,name="contact_us_view"),
            path("contact/us/add",views.add_contact_us_view,name="add_contact_us_view"),
            path("contact/us/all",views.contact_us_all_view,name="contact_us_all_view")]