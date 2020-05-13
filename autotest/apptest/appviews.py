from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AppCase, AppCaseStep
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Create your views here.


@login_required
def appcase_manage(request):
    username = request.session.get('user', '')
    appcase_list = AppCase.objects.all()
    appcase_count = AppCase.objects.all().count()
    paginator = Paginator(appcase_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcase_list = paginator.page(currentPage)
    except PageNotAnInteger:
        appcase_list = paginator.page(1)
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)
    return render(request, 'appcase_manage.html',
                  {"user": username, 'app_cases': appcase_list, 'appcase_count': appcase_count})


@login_required
def appcasestep_manage(request):
    username = request.session.get('user', '')
    appcasestep_list = AppCaseStep.objects.all()
    appcasestep_count = AppCaseStep.objects.all().count()
    paginator = Paginator(appcasestep_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcasestep_list = paginator.page(currentPage)
    except PageNotAnInteger:
        appcasestep_list = paginator.page(1)
    except EmptyPage:
        appcasestep_list = paginator.page(paginator.num_pages)
    return render(request, 'appcasestep_manage.html',
                  {'user': username, 'app_case_steps': appcasestep_list, 'appcasestep_count': appcasestep_count})


@login_required
def appcase_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('app_case_name', '')
    app_list = AppCase.objects.filter(app_case_name__icontains=search_name)
    return render(request, 'appcase_manage.html', {'user': username, 'app_cases': app_list})


@login_required
def appstep_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('app_test_step', '')
    app_list = AppCaseStep.objects.filter(app_test_step__icontains=search_name)
    return render(request, 'appcasestep_manage.html', {'user': username, 'app_case_steps': app_list})
