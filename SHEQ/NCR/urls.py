from django.urls import path
from. import views

urlpatterns = [
    path('NCR_Main/', views.ncr_menu_views, name = "NCR_home_page"),



]
