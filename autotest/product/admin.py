from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # 设置列表可显示的字段
    list_display = ('id', 'product_name', 'product_desc', 'producter', 'create_time',)

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
