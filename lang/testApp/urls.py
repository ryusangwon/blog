from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.index, name='index'),
    path('user/<int:pk>/', views.word_detail, name='word-detail'),
]
