from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.home_views, name = "home_page"),
    path('login/', views.login_views, name = "login_view"),
    path('sign_in/', views.signin_views, name = "signin_view"),
    path('company/', views.registerCompany, name="company"),

]
