from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<int:post_id>/edit/', post_edit, name='post_edit'),
    path('<int:post_id>/delete/', post_delete, name='post_delete'),
    path('register/', register, name='register'),
    
]