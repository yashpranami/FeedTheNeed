from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('request/', views.request, name='request'),
    #path('donate/request', views.request, name='request'),
    #path('donate/home', views.home , name='home'),

]
