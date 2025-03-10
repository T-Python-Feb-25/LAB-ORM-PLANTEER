
from django.urls import path
from . import views
app_name="plants"
urlpatterns=[path("new/",views.create_view,name="create_view"),
             path('search/',views.search_view,name="search_view"),
             path("all/",views.all_plants_view,name="all_plants_view"),
             path("<plant_id>/detail/",views.plant_detail_view,name="plant_detail_view"),
             path("<plant_id>/update/",views.update_view,name="update_view"),
             path("<plant_id>/delate/",views.delate_view,name="delate_view"),
            path("reviews/add/<plant_id>/",views.add_comment_view,name="add_comment_view"),
           
            ]