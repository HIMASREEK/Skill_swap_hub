from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_list, name='skill_list'),
    path('add/', views.skill_add, name='skill_add'),
    path('edit/<int:pk>/', views.skill_edit, name='skill_edit'),
]