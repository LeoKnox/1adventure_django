from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.display_room, name='display_room'),
    path('<int:room_id>/edit/', views.edit_room, name='edit_room')
]