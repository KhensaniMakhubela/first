from django.db import models
from django.contrib.auth.models import User
from auth_site.models import Company, Process


class ISO_Clauses(models.Model):
    clause_name = models.CharField(max_length=50)

    def __str__(self):
        return self.clause_name


class Doc_type(models.Model):
    type = models.CharField(max_length=20)
    def __str__(self):
        return str(self.type)


class Frequency(models.Model):
    months = models.IntegerField()
    def __str__(self):
        return str(self.months)


class Status (models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return str(self.status)


class Document(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    document_name = models.ForeignKey(Process, on_delete=models.CASCADE, null= True)
    clause_name = models.ForeignKey(ISO_Clauses, on_delete=models.CASCADE)
    document_type = models.ForeignKey(Doc_type, on_delete=models.CASCADE, null = True)
    purpose = models.TextField()
    scope = models.TextField()
    document_owner = models.ForeignKey(User, on_delete= models.CASCADE)
    revision_frq = models.ForeignKey(Frequency, on_delete=models.CASCADE, null=True)
    review_on = models.DateField()
    approved_on = models.DateField(null = True)
    revision = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self. document_name) + " - Rev no.: " + str(self. revision)


class Doc_details(models.Model):
    procedure_name = models.ForeignKey(Document, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    responsible_person = models.ForeignKey(User, on_delete= models.CASCADE)
    review_on = models.DateField()
    revision_frq = models.ForeignKey(Frequency, on_delete=models.CASCADE, null=True)
    revision = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    details = models.TextField()
    def __str__(self):
        name = str(self.procedure_name)
        return name





