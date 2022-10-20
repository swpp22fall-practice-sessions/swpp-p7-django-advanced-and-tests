from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/', views.id, name='hero_id'),
    path('info/', views.hero_list, name='hero_list'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
    path('token/', views.token, name='token'),
]