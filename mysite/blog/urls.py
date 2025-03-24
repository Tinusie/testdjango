from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.post_list, name='post_list'),
]