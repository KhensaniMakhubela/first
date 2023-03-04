from .models import Company
from django.forms import ModelForm

class registerCompany(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        #
        # widgets = {
        # "company_name" : forms.TextInput(attrs = {'class' : "form-control"}),
        # "branch" : forms.TextInput(attrs = {'class' : "form-control"}),
        # "contact" : forms.TextInput(attrs = {'class' : "form-control"}),
        # "industry" : forms.Select(attrs = {'class' : "form-control"}),
        # "country" : forms.Select(attrs = {'class' : "form-control"}),
        # "department" : forms.SelectMultiple(attrs = {'class' : "form-control"})
        #
        # }
