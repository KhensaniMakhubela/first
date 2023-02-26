from datetime import datetime


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ISO_Clauses, Document, Doc_details, Frequency,Doc_type, Status
from auth_site.models import User_added_info, Process, Company, Status, Department
from django.contrib.auth.models import User


@login_required  # Home view
def ms_home_views(request):

    user = request.user
    user_infor = User_added_info.objects.get(user = user)
    menulist = ISO_Clauses.objects.all()
    procedures_list = Document.objects.filter(company = user_infor.company, status = 1)


    return render(request, "MS/template/main.html", context= {"menulst" : menulist, "current_user" : user_infor  , "procedure_list" : procedures_list })


@login_required  # Listing all the procedure
def ms_procedures(request, id):

    details = Doc_details.objects.filter(procedure_name=id)
    document_details = Document.objects.get(id=id)


    return render(request, "MS/template/user_page.html", context= {"details" : details, "main_doc": document_details })


@login_required  #update the procedure
def ms_update(request, id):
    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.filter(procedure_name=id)

    document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)


    if request.method == 'POST':

        changeDocstatus = Document.objects.get(id=id)
        changeDocstatus.status = Status(id = 3)
        changeDocstatus.save()
        purpose = request.POST['purpose']
        scope = request.POST['scope']

        if request.POST["document_owner"] == "document_owner":
            document_owner = document_details.document_owner
        else:
            document_owner = User.objects.get(username=request.POST["document_owner"])

        revision_frqcy = Frequency.objects.get(id= request.POST["revision_frqcy"])

        updated_doc = Document(
            company = document_details.company,
            document_name=document_details.document_name,
            clause_name=document_details.clause_name,
            document_type=document_details.document_type,
            purpose=purpose,
            scope=scope,
            document_owner=document_owner,
            revision_frq= revision_frqcy,
            review_on=datetime.now(),
            revision=document_details.revision + 1,
            status = Status(id = 1)
        )


        updated_doc.save()


        return redirect("MS_home_page")

    return render(request, "MS/template/update.html", context= {"details" : details, "main_doc": document_details , "user_infor": user_infor, "frqs": frq})


@login_required  # Create document
def ms_Doc_create(request):

    user = request.user
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    revision_frqcy = Frequency.objects.all()
    clause = ISO_Clauses.objects.all()
    doc_type = Doc_type.objects.all()

    process = Process.objects.filter(company = company.company)

    if request.method == 'POST' :
        document_name = Process.objects.get(id = request.POST["document_name"])
        clause_name = ISO_Clauses.objects.get( id =  request.POST["clause_name"])
        document_type = Doc_type.objects.get(id = request.POST["document_type"])
        purpose = request.POST['purpose']
        scope = request.POST['scope']
        document_owner = User.objects.get(username = request.POST['document_owner'])
        revision_frqcy = Frequency.objects.get(id = request.POST["revision_frqcy"])

        updated_doc = Document(
            company = company.company,
            document_name=document_name,
            clause_name=clause_name,
            document_type=document_type,
            purpose=purpose,
            scope=scope,
            document_owner=document_owner,
            revision_frq= revision_frqcy,
            review_on=datetime.now(),
            revision= 0,
            status = Status(id = 1)
        )

        updated_doc.save()
        return redirect("MS_home_page")

    return render(request, "MS/template/create_Doc.html", context= {"processes":process ,"user_infor": user_infor, "clause_list": clause, "doc_type" : doc_type, "revision_frqcy":revision_frqcy})


@login_required  # Create document
def process(request):

    user = request.user
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)
    process = Process.objects.filter(company = company.company)

    return render(request, "MS/template/process.html", context= {"processes":process ,"user_infor": user_infor, "company": company})


@login_required  # Create document
def process_create(request):

    user = request.user
    company = User_added_info.objects.get(user=user)
    department = Company.objects.get(company_name=company.company)
    department_list =  department.department.all()
    user_infor = User_added_info.objects.filter(company=company.company)
    process = Process.objects.filter(company = company.company)

    if request.method == 'POST' :
        department_ = Company.department.objects.get( department =  request.POST.get("department"))


        process = request.POST["process"]
        status = Status(id = 1)

        process(
                department = department_,
                process = process,
                ststus = status
                )

        process.save()
        return redirect("MS_home_page")

    return render(request, "MS/template/create_process.html", context= { "company": company, "department": department_list})


@login_required
def ms_update_detail(request, id):
    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    return render(request, "MS/template/update_detail.html", context= {"details" : details , "user_infor": user_infor, "frqs": frq})

@login_required
def ms_Doc_Detail_create(request, id ):
    frq = Frequency.objects.all()
    user = request.user
    document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    return render(request, "MS/template/create_detail.html", context= { "user_infor": user_infor, "frqs": frq, "document_details": document_details})


@login_required
def createDetailview(request):
    frq = Frequency.objects.all()
    user = request.user
    # document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    if request.method == 'POST':
        procedure_name = Document.objects.get( id = request.POST["procedure_name"])
        title = request.POST["title"]
        responsible_person = User.objects.get(username=request.POST['responsible_person'])

        revision_frq = Frequency.objects.get(id = request.POST["revision_frq"])
        details = request.POST["details"]

        doc_details = Doc_details(
            procedure_name=procedure_name,
            title= title,
            responsible_person=responsible_person,
            review_on=datetime.now(),
            revision_frq=revision_frq,
            revision=0,
            status= Status(id=1),
            details=details
        )

        doc_details.save()
        return redirect("MS_home_page")



        doc_details.save()
        return redirect("MS_home_page")

    return render(request, "MS/template/create_detail.html", context={"user_infor": user_infor, "frqs": frq})