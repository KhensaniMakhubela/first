from django.contrib import admin
from .models import Company,Industry,Country, State, Job_title, User_added_info, Department, Process, Status

# Register your models here.

admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Job_title)
admin.site.register(Department)

admin.site.register(User_added_info)
admin.site.register(Process)
admin.site.register(Status)