from django.urls import path
from. import views

urlpatterns = [
    path('', views.ms_home_views, name = "MS_home_page"),
    path('View/<str:id>/',views.ms_procedures, name='procedure_view'),
    path('update/<str:id>/',views.ms_update, name='update_view'),
    path('detail/<str:id>/update',views.ms_update_detail, name='update_detail_view'),

    path('create_document/',views.ms_Doc_create, name='create_doc_view'),
]
