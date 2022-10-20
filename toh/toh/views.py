from django.contrib import admin
from django.urls import URLPattern, include, path

urlpatterns = [
    path('hero/', include('hero.urls')),
    path('admin/', admin.site.urls),
    
]