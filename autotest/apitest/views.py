from django.shortcuts import render
from django.http import HttpResponse  # 加入引用
from django.contrib import auth
from django.http import HttpResponseRedirect


# Create your views here.
def test(request):
    return HttpResponse("hello test")  # 返回HttpResponse响应函数


# django登录实现
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')


# 前台首页

def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
