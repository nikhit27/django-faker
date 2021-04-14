from django.urls import path, include
from app1 import views

urlpatterns = [
    path('index/', views.index_page),
    path('temp/',views.welcome_page),
]
