from django.urls import path
from. import views

urlpatterns = [
    path('', views.ms_home_views, name = "MS_home_page"),
    path('View/<str:id>/',views.ms_procedures, name='procedure_view'),
    path('update/<str:id>/',views.ms_update, name='update_view'),
    path('detail/<str:id>/review',views.ms_update_detail, name='update_detail_view'),

    path('Process/', views.process, name='process'),
    path('Process/create/', views.process_create, name='process_create'),

    path('detail/<str:id>/obsolete',views.ms_update_detail, name='update_detail_view'),
    path('create_document/',views.ms_Doc_create, name='createDocView'),
    path('create_document/<int:id>/create_section/', views.ms_Doc_Detail_create, name='createDocDetailview'),
    path('create_document/create_section/', views.createDetailview, name='createDetailview'),
]
