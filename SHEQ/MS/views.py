from datetime import datetime


from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import ISO_Clauses, Document, Doc_details, Frequency,Doc_type, Status
from auth_site.models import User_added_info, Process, Company, Department
from auth_site.models import Status as auth_status
from django.contrib.auth.models import User


@login_required  # Home view
def ms_home_views(request):

    user = request.user
    user_infor = User_added_info.objects.get(user = user)
    menulist = ISO_Clauses.objects.all()
    procedures_list = Document.objects.filter(company = user_infor.company, status = 3)


    return render(request, "MS/template/main.html", context= {"menulst" : menulist, "current_user" : user_infor  , "procedure_list" : procedures_list })


@login_required  # Listing all the procedure
def processProcedure(request, id):

    username = request.user
    company = User_added_info.objects.get(user=username)
    process = Process.objects.get(id = id)

    document_name = Document.objects.get(company = company.company, document_name = process,  status = (Status (id=3)))

    return ms_procedures(request,document_name.id )


@login_required  # Listing all the procedure
def ms_procedures(request, id):



    document_details = Document.objects.get(id=id, status = Status(id = 3))
    process = Process.objects.get(process = document_details.document_name)
    details = Doc_details.objects.filter(procedure_name=process.id)

    return render(request, "MS/template/user_page.html", context= {"details" : details, "main_doc": document_details })


@login_required  #update the procedure
def ms_update(request, id):

    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.filter(procedure_name=id)

    document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    # if Document.objects.filter(document_name=document_details.document_name, status=Status(id=2)) :
    #     redirect(request, "approve_item")


    if request.method == 'POST':

        # changeDocstatus = Document.objects.get(id=id)
        # changeDocstatus.status = Status(id = 3)
        # changeDocstatus.save()

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
            status = Status(id = 2)
        )

        updateProcess = Process.objects.get(process = document_details.document_name)
        updateProcess.status =  auth_status(id = 2)

        updateProcess.save()
        updated_doc.save()

        return redirect("MS_home_page")

    return render(request, "MS/template/update.html", context= {"details" : details, "main_doc": document_details , "user_infor": user_infor, "frqs": frq,})


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
            status =  Status(id = 3)
        )
        updated_doc.save()

        updateProcess = Process.objects.get(process = document_name)
        updateProcess.status =  auth_status(id = 2)
        updateProcess.save()

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
        cmpy = Company.objects.get( company_name = company.company)
        department_ = Department.objects.get(id = (request.POST["department"]))
        process_ = str(request.POST["process"]).strip()

        try:
            process_inst = Process(
                company=cmpy,
                department=department_,
                process=process_,
                status=auth_status(id=1)
            )

            process_inst.save()
            return redirect("process")

        except IntegrityError:

            return render(request, "MS/template/create_process.html", {'error': 'The process is already registered in this department',  "company": company, "department": department_list})

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

    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    if request.method == 'POST':

        procedure_name = request.POST['procedure_name']
        document_name = Process.objects.get(process = str(procedure_name).strip())
        title = request.POST["title"]
        responsible_person = User.objects.get(username=request.POST['responsible_person'])

        revision_frq = Frequency.objects.get(id = request.POST["revision_frq"])
        details = request.POST["details"]

        doc_details = Doc_details(
            procedure_name=document_name,
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


@login_required  # Create document
def approval_list(request):

    company = User_added_info.objects.get(user=request.user)
    documents = Document.objects.filter(company = company.company, status=Status(id=2))
    # Process.objects.get()

    return render(request, "MS/template/approveLst.html", context= {"documents":documents })


# def approval_Doc(request, id):
#     company = User_added_info.objects.get(user=request.user)
#     documents = Document.objects.filter(id = id, company=company.company, status=Status(id=2))
#     print(documents)
#     ms_procedures(request, id)
#     return render(request, "MS/template/approveLst.html", context={"documents": documents})

def approval_Doc(request, id):

    old_documents = Document.objects.get(id = id)
    old_documents.status = Status(id=1)
    old_documents.save()

    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.filter(procedure_name=id)

    document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    if request.method == 'POST':

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
            approved_on=datetime.now(),
            revision=document_details.revision,
            status = Status(id=1)
        )


        updated_doc.save()

        return redirect("MS_home_page")

    return render(request, "MS/template/approve.html", context= {"details" : details, "main_doc": document_details , "user_infor": user_infor, "frqs": frq,})