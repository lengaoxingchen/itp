from django.shortcuts import render
from .models import Set
from django.contrib.auth.models import User  # 引入Django自带木星auth.models 把用户管理的功能加入到系统设置中


# Create your views here.

def set_manage(request):
    set_list = Set.objects.all()
    username = request.session.get('user', '')
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list})


def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user', '')
    return render(request, 'set_user.html', {'user': username, 'users': user_list})
