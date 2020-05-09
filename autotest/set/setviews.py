from django.shortcuts import render
from .models import Set
from django.contrib.auth.models import User  # 引入Django自带木星auth.models 把用户管理的功能加入到系统设置中
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def set_manage(request):
    set_list = Set.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(set_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        set_list = paginator.page(currentPage)
    except PageNotAnInteger:
        set_list = paginator.page(1)
    except EmptyPage:
        set_list = paginator.page(paginator.num_pages)
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list})


def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(user_list, 8)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        user_list = paginator.page(currentPage)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    return render(request, 'set_user.html', {'user': username, 'users': user_list})


@login_required
def set_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('set_name', '')
    set_list = Set.objects.filter(set_name__icontains=search_name)
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list})


@login_required
def user_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('username', '')
    user_list = Set.objects.filter(username__icontains=search_name)
    return render(request, 'set_user.html', {'user': username, 'users': user_list})
