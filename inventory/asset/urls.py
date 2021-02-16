from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('check/', views.check, name='check'),
    path('register/', views.register, name='register'),
    path('inventory/', views.inventory, name='inventory'),
    path('viewasset/', views.viewasset, name='viewasset'),
    path('addasset/', views.addasset, name='addasset'),
    path('editasset/<int:ids>', views.editasset, name='editasset'),
    path('deleteasset/<int:ids>/', views.deleteasset, name='deleteasset'),
    path('updateasset/<int:ids>', views.updateasset, name='updateasset'),
    path('viewcat/', views.viewcat, name='viewcat'),
    path('addcat/', views.addcat, name='addcat'),
    path('editcat/<int:ids>', views.editcat, name='editcat'),
    path('deletecat/<int:ids>/', views.deletecat, name='deletecat'),
    path('updatecat/<int:ids>', views.updatecat, name='updatecat'),
]