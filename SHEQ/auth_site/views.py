from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Job_title,Company, Department, User_added_info
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_views(request):

    return render(request, "auth_site/template/login_home.html")


def login_views(request):

    if request.method == "POST":
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']

        user = authenticate(username=user_name, emmail = email, password=password1, )
        if user is not None:
            login(request, user)
            return redirect("MS_home_page")
        else:
            messages.info(request, "invalid login credentials")
            return render(request, "auth_site/template/login.html")

    return render(request, "auth_site/template/login.html")


def signin_views(request):

    company_info = Company.objects.all()
    department = Department.objects.all()
    job_title = Job_title.objects.all()

    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        try:
            company = request.POST['company']
            department = request.POST['department']
            job_title = request.POST['job_title']
        except:
            messages.info(request, "Please complete the form correctly")
            return redirect("signin_view")

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 and password1 != "" and first_name != "" and user_name != ""  and last_name != "" and email != "":

            user = User.objects.create_user(username=user_name,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=password1)

            company = Company.objects.get(id=company)
            print(company)
            department = Department.objects.get(id=department)
            job_title = Job_title.objects.get(id=job_title)

            added_info = User_added_info(user = user, company = company, department = department, job_title =job_title)

            user.save(); added_info.save()

            return redirect("home_page")

        elif User.objects.filter(username = user_name):
            messages.info(request, "username exist")
            return redirect("signin_view")

        elif User.objects.filter(first_name = first_name):
            messages.info(request, "first name exist")
            return redirect("signin_view")

        else:
            messages.info(request, "Form not filled in correctly, Please try again!")
            return redirect("signin_view")

    else:
        return render(request, "auth_site/template/signin.html", {"department_list":department, "company_list":company_info, "jobtitle_list": job_title })






