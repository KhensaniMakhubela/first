from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


# company table
class Industry(models.Model):
    industry = models.CharField(max_length=25)

    def __str__(self):
        return self.industry


class Country(models.Model):
    country = models.CharField(max_length= 20)

    def __str__(self):
        return self.country


class State(models.Model):
    state_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class Department(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length= 100)
    branch = models.CharField(max_length= 100)
    contact = models.CharField(max_length=10)
    industry = models.ForeignKey(Industry, on_delete= models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department, null = True, blank = True)

    def __str__(self):
        return self.company_name


# job title
class Job_title(models.Model):
    title_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title_name




class Status (models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return str(self.status)


class Process(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE, blank = False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    process = models.CharField(max_length= 150)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.process
    class Meta:
        ordering = ['-department']
        constraints = [
            models.UniqueConstraint(fields=['department', 'process'], name='dpt_process')
        ]



class User_added_info(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    company = models.ForeignKey(Company, on_delete= models.CASCADE, blank = False)
    department = models.ForeignKey(Department, on_delete= models.CASCADE, blank = False)
    job_title = models.ForeignKey(Job_title, on_delete=models.CASCADE, blank = False)

    def __str__(self):
        return str(self.user)






