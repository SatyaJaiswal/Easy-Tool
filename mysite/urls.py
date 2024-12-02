# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the home app URLs
    path('bgRemover/', include('bgRemover.urls')),  # Include the bgRemover app URLs
    path('msWord_pdf/', include('msWord_pdf.urls')) ,
]
