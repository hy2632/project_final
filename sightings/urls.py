from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.index, name='index'),
    path('stats',views.stats),
    path('add',views.add),
    path('<str:sqr_id>',views.update),
]

