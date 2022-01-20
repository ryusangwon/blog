from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user_list, name='user-list'),
    path('user/new/', views.user_create, name='user-create'),
    path('user/<int:user_id>/', views.user_detail, name='user-detail'),
]
