from django.contrib import admin
from .models import Product
from apitest.models import Apis, ApiTest
from apptest.models import AppCase
from webtest.models import WebCase


# Register your models here.

class ApisAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param_value', 'api_method', 'api_result', 'api_status', 'create_time',
                    'id', 'product', ]
    model = Apis
    extra = 1


class AppCaseAdmin(admin.TabularInline):
    list_display = ['id', 'app_case_name', 'app_test_result', 'create_time', 'product']
    model = AppCase
    extra = 1


class WebCaseAdmin(admin.TabularInline):
    list_display = ['id', 'web_case_name', 'web_test_result', 'create_time', 'product']
    model = WebCase
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ['id', 'product_name', 'product_desc', 'producter', 'create_time', ]
    inlines = [ApisAdmin, AppCaseAdmin, WebCaseAdmin]

    # 下面过滤项目可根据实际情况确定是否取消注释
    # # 设置过滤选项
    # list_filter = ('producter',)
    #
    # # 每页显示条目数
    # list_per_page = 5
    #
    # # 设置可编辑字段
    # list_editable = ('producter',)
    #
    # # 按日期月份筛选
    # date_hierarchy = 'create_time'
    #
    # # 按发布日期排序
    # ordering = ('-create_time',)


admin.site.register(Product, ProductAdmin)  # 把产品模块注册到Django admin 后台并能显示
