from django.shortcuts import render
from django.http import HttpResponse  # 加入引用
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import ApiTest, ApiStep, Apis
from django.contrib.auth.decorators import login_required
import pymysql
import HTMLTestRunner


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


# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()  # 读取所有流程接口数据
    username = request.session.get('user', '')  # 读取浏览器登录session
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list})  # 定义流程接口数据并返回给前端


# 接口步骤管理
@login_required
def apistep_manage(request):
    apistep_list = ApiStep.objects.all()
    username = request.session.get('user', '')
    return render(request, "apistep_manage.html", {"user": username, "apisteps": apistep_list})


# 单一接口管理
@login_required
def apis_manage(request):
    apis_list = Apis.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apis_manage.html', {'user': username, 'apis': apis_list})


# 测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()  # 统计接口数
    db = pymysql.connect(user='root', db='autotest', password='123456', host='123.57.135.88', port=3306)
    cursor = db.cursor()
    pass_sql = 'select count(id) from autotest.apitest_apis where apitest_apis.api_status=1'
    aa = cursor.execute(pass_sql)
    api_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    fail_sql = 'select count(id) from autotest.apitest_apis where apitest_apis.api_status=0'
    bb = cursor.execute(fail_sql)
    api_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, 'report.html',
                  {'user': username, 'apis': apis_list, 'apis_count': apis_count, 'api_pass_count': api_pass_count,
                   'api_fail_count': api_fail_count})  # 把值赋值给apis_count变量


def left(request):
    return render(request, 'left.html')
