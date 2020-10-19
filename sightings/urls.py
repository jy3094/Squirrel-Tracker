from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.show_map, name='show_map'),
    path('add/', views.add, name='add'),
    path('<squirrel_id>/', views.detail, name='detail')
]
