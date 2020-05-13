from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WebCase, WebCaseStep
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


@login_required
def webcase_manage(request):
    username = request.session.get('user', '')
    webcase_list = WebCase.objects.all()
    webcase_count = WebCase.objects.all().count()
    paginator = Paginator(webcase_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        webcase_list = paginator.page(currentPage)
    except PageNotAnInteger:
        webcase_list = paginator.page(1)
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages)
    return render(request, 'webcase_manage.html',
                  {"user": username, 'web_cases': webcase_list, 'webcase_count': webcase_count})


@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    webcasestep_list = WebCaseStep.objects.all()
    webcasestep_count = WebCaseStep.objects.all().count()
    paginator = Paginator(webcasestep_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        webcasestep_list = paginator.page(currentPage)
    except PageNotAnInteger:
        webcasestep_list = paginator.page(1)
    except EmptyPage:
        webcasestep_list = paginator.page(paginator.num_pages)
    return render(request, 'webcasestep_manage.html',
                  {'user': username, 'web_case_steps': webcasestep_list, 'webcasestep_count': webcasestep_count})


@login_required
def webcase_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('web_case_name', '')
    web_list = WebCase.objects.filter(web_case_name__icontains=search_name)
    return render(request, 'webcase_manage.html', {'user': username, 'web_cases': web_list})


@login_required
def webstep_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('web_test_step', '')
    web_list = WebCaseStep.objects.filter(web_test_step__icontains=search_name)
    return render(request, 'webcasestep_manage.html', {'user': username, 'web_case_steps': web_list})
