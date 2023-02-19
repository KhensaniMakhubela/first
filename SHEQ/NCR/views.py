from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.

@login_required
def ncr_menu_views(request):
    user = request.user
    email = request.user.email


    return render(request, "NCR/template/main_menu.html", {'user': user, "email":email })

