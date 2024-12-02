# bgRemover/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.msWord_pdf, name='msWord_pdf'),  # URL for the main page
    path('msWord-pdf/', views.msWord_pdf, name='msWord-pdf'),  # URL for background removal API 
]
