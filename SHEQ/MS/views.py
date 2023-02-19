from datetime import datetime
from .form import DocumentForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ISO_Clauses, Document, Doc_details, Frequency,Doc_type, Status
from auth_site.models import User_added_info
from django.contrib.auth.models import User


@login_required  # Home view
def ms_home_views(request):

    user = request.user
    user_infor = User_added_info.objects.get(user = user)
    menulist = ISO_Clauses.objects.all()
    procedures_list = Document.objects.filter(company = user_infor.company)


    return render(request, "MS/template/main.html", context= {"menulst" : menulist, "current_user" : user_infor  , "procedure_list" : procedures_list })


@login_required  # Listing all the procedure
def ms_procedures(request, id):

    details = Doc_details.objects.filter(procedure_name=id)
    document_details = Document.objects.get(id=id)
    loop_value = 1

    return render(request, "MS/template/user_page.html", context= {"details" : details, "main_doc": document_details, "loop_value":loop_value})


@login_required  #update the procedure
def ms_update(request, id):
    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.filter(procedure_name=id)

    document_details = Document.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    if request.method == 'POST':
        # def check_change():
        #     if request.POST["purpose"] == document_details.purpose:
        #         return True
        #     else: return False

        purpose = request.POST['purpose']
        scope = request.POST['scope']
        document_owner = User.objects.get( id = request.POST["document_owner"])
        print(document_owner)

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
            revision=document_details.revision + 1
        )

        updated_doc.save()
        return redirect("MS_home_page")

    return render(request, "MS/template/update.html", context= {"details" : details, "main_doc": document_details , "user_infor": user_infor, "frqs": frq})


@login_required  # Create document
def ms_Doc_create(request):

    form = DocumentForm()
    user = request.user
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    revision_frqcy = Frequency.objects.all()
    clause = ISO_Clauses.objects.all()
    doc_type = Doc_type.objects.all()

    if request.method == 'POST' :





        document_name = request.POST["document_name"]
        clause_name = ISO_Clauses.objects.get( id =  request.POST["clause_name"])
        document_type = Doc_type.objects.get(id = request.POST["document_type"])
        purpose = request.POST['purpose']
        scope = request.POST['scope']
        document_owner = User.objects.get(username = request.POST['document_owner'])
        revision_frqcy = request.POST["revision_frqcy"]

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
            # status = Status(id = 4)
        )

        updated_doc.save()
        return redirect("MS_home_page")

    return render(request, "MS/template/create_Doc.html", context= {"user_infor": user_infor, "clause_list": clause, "doc_type" : doc_type, "revision_frqcy":revision_frqcy, "form":form})


@login_required
def ms_update_detail(request, id):
    frq = Frequency.objects.all()
    user = request.user
    details = Doc_details.objects.get(id=id)
    company = User_added_info.objects.get(user=user)
    user_infor = User_added_info.objects.filter(company=company.company)

    return render(request, "MS/template/update_detail.html", context= {"details" : details , "user_infor": user_infor, "frqs": frq})

