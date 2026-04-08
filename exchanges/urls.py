from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange_list, name='exchange_list'),
    path('create/<int:skill_id>/', views.exchange_create, name='exchange_create'),
    path('request/<int:pk>/', views.request_detail, name='exchange_detail'),
    path('request/<int:pk>/accept/', views.exchange_accept, name='exchange_accept'),
    path('request/<int:pk>/reject/', views.exchange_reject, name='exchange_reject'),
    path('request/<int:pk>/review/', views.exchange_review, name='exchange_review'),
]