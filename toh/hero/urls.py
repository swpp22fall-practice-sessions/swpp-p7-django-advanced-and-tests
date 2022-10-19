from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.hero_list),
    path('<int:id>/', views.id, name='hero_id'),
    # path('<str:name>/', views.name, name='hero_name'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
    path('admin/', admin.site.urls),
    path('token/', views.token, name='token')
]