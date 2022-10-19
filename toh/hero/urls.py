from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.hero_list),
    path('', views.index),
    path('<int:id>/', views.id, name='hero_id'),
    # path('<str:name>/', views.name, name='hero_name'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
    path('token/', views.token, name='token')
]