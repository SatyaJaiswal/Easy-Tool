# bgRemover/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bgRemover_view, name='bgRemover'),  # URL for the main page
    path('remove-background/', views.remove_background, name='remove_background'),  # URL for background removal API 
]
