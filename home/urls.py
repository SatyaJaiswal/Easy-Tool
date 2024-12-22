from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('submit-review/', views.submit_review, name='submit_review'),
]
