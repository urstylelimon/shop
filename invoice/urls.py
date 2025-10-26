from django.urls import path
from . import views

urlpatterns = [

    #Customer Urls--------------------------
    path('create_customer/', views.create_customer, name='create_customer'),
    path('all_customer/', views.all_customer, name='all_customer'),
    path('single_customer/<int:pk>/', views.single_customer, name = 'single_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),

    #Product Urls-------------------------------
    path('product_list/', views.product_list, name='product_list'),

# Invoice--------------------------------------------------------------------------------------
    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('all_invoice/', views.all_invoice, name='all_invoice'),
    path('single_invoice/<int:pk>/', views.single_invoice, name = 'single_invoice'),
    path('update_invoice/<int:pk>/', views.update_invoice, name='update_invoice'),
    path('transaction/', views.transaction, name='transaction'),
]