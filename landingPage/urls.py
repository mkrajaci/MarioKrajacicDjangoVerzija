from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingPage-home'),
    path('about/', views.home_about, name='landingPage-about'),
]
