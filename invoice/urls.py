from django.urls import path
from . import views

urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('all_customer/', views.all_customer, name='all_customer'),
    path('single_customer/<int:pk>/', views.single_customer, name = 'single_customer'),
]