from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index),    
    path('sightings/', views.index),
    path('sightings/<squirrel_id>/', views.detail, name='detail'),
    path('map/',views.map, name='map'),
]

