from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WebCase, WebCaseStep


# Create your views here.


@login_required
def webcase_manage(request):
    username = request.session.get('user', '')
    webcase_list = WebCase.objects.all()
    return render(request, 'webcase_manage.html', {"user": username, 'web_cases': webcase_list})


@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    webcasestep_list = WebCaseStep.objects.all()
    return render(request, 'webcasestep_manage.html', {'user': username, 'web_case_steps': webcasestep_list})
