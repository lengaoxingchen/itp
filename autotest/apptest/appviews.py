from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AppCase, AppCaseStep


# Create your views here.


@login_required
def appcase_manage(request):
    username = request.session.get('user', '')
    appcase_list = AppCase.objects.all()
    return render(request, 'appcase_manage.html', {"user": username, 'app_cases': appcase_list})


@login_required
def appcasestep_manage(request):
    username = request.session.get('user', '')
    appcasestep_list = AppCaseStep.objects.all()
    return render(request, 'appcasestep_manage.html', {'user': username, 'app_case_steps': appcasestep_list})
