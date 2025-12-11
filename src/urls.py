from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('injection/', views.injection, name = 'injection'),
  path('access/', views.access, name = 'access'),
  path('cryptography/', views.cryptography, name = 'cryptography'),
  path('injection/add/', views.add, name = 'add')
]