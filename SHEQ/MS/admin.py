from django.contrib import admin
from .models import ISO_Clauses,Document,Doc_details, Doc_type,Frequency,Status
# Register your models here.

admin.site.register(ISO_Clauses)
admin.site.register(Document)
admin.site.register(Doc_details)
admin.site.register(Doc_type)
admin.site.register(Frequency)
admin.site.register(Status)