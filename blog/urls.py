from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('bloghome/', views.bloghome, name='bloghome'),
    path('search/', views.search, name='search'),
    path('user/', views.user, name='user'),

]