from django.shortcuts import render
from .models import Bug
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

# bug 管理
def bug_manage(request):
    bug_list = Bug.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(bug_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        bug_list = paginator.page(currentPage)
    except PageNotAnInteger:
        bug_list = paginator.page(1)
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})


@login_required
def bug_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('bug_name', '')
    bug_list = Bug.objects.filter(bug_name__icontains=search_name)
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})
