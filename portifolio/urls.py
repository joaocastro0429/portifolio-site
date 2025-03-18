from django.urls import path
from .import views

urlpatterns = [
    path('portifolio/', views.home, name="home"),
    
]
