from django.urls import path
from . import views

app_name = 'plants'
urlpatterns = [
    path('all/',views.all_plants_view,name='all_plants_view'),
    path('new/',views.add_plant_view,name='add_plant_view'),
    path('<plant_id>/detail/',views.plant_detail_view,name='plant_detail_view'),
    path('<plant_id>/update/',views.plant_update_view,name='plant_update_view'),
    path('<plant_id>/delete/',views.plant_delete_view,name='plant_delete_view'),
    path('search/',views.search_plant_view,name='search_plant_view'),
    path('<plant_id>/detail/comment/',views.add_comment_view,name='add_comment_view')
]




''''
- Home page `/`
- All Plants page : `plants/all/`
- Plant Detail Page : `plants/<plant_id>/detail/`
- Add new plant page : `plants/new/`
- Update plant page : `plants/<plant_id>/update/`,
- Delete Plant : `plants/<plant_id>/delete/`
- Search Page : `plants/search/`
- (Bonus) Contact Us page : `contact/`
- (Bonus) Contact Us Messages page : `contact/messages/`
'''
