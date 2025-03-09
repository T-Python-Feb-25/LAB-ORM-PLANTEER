from django.urls import path
from . import views


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

app_name = 'main'
urlpatterns = [
    path('',views.home_view,name='home_view')
]
