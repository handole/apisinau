from django.urls import path
from . import views

urlpatterns = [
    path('', views.sinaus, name='sinaus'),
    path('add', views.add_sinau, name='addsinau'),
    path('<int:id>/video/add', views.add_video, name='addvideo'),
    path('<int:id>/video', views.videos, name='vides'),
]