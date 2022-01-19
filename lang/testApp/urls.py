from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.index, name='index'),
    path('user/new/', views.user_create, name='user-create'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
]
