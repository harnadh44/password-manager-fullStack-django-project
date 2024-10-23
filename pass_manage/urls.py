from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('upload/', views.upload, name="upload"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('myaccount/', views.my_account, name='my_account'),
    path('getDetails', views.getDetails, name="getDetails")
]