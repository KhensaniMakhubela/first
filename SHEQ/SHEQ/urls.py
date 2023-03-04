from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("auth_site.urls")),
    path('NCR/', include("NCR.urls")),
    path('Management_System/', include("MS.urls")),

]
