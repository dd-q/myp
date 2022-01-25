from django.contrib import admin
from django.urls import path, include
from postapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('postapp.urls')),
    
]
