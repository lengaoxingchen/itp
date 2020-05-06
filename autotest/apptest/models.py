from django.db import models
from product.models import Product


# Create your models here.

class AppCase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    app_case_name = models.CharField('用例名称', max_length=200)  # 测试用例名称
    app_test_result = models.BooleanField('测试结果')  # 测试结果
    app_tester = models.CharField('测试负责人', max_length=16)  # 测试负责人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.app_case_name


class AppCaseStep(models.Model):
    AppCase = models.ForeignKey(AppCase, on_delete=models.CASCADE, null=True)  # 关联接口Id
    app_test_step = models.CharField('测试步骤', max_length=200)  # 测试步骤
    app_test_objname = models.CharField('测试对象名称描述', max_length=200)  # 测试对象名称描述
    app_opt_method = models.CharField('定位方式', max_length=200)  # 定位方式
    app_ev_element = models.CharField('控件元素', max_length=800)  # 控件元素
    app_test_date = models.CharField('测试数据', max_length=200, null=True)  # 测试数据,临时增加字段时要设置可为空
    app_assert_data = models.CharField('校验数据', max_length=200)  # 校验数据
    app_test_result = models.BooleanField('测试结果')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    def __str__(self):
        return self.app_test_step
