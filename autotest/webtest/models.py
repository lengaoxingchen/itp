from django.db import models
from product.models import Product


# Create your models here.

class WebCase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    web_case_name = models.CharField('用例名称', max_length=200)  # 测试用例名称
    web_test_result = models.BooleanField('测试结果')  # 测试结果
    web_tester = models.CharField('测试负责人', max_length=16)  # 测试负责人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'

    def __str__(self):
        return self.web_case_name


class WebCaseStep(models.Model):
    WebCase = models.ForeignKey(WebCase, on_delete=models.CASCADE, null=True)  # 关联接口Id
    # web_test_name = models.CharField('测试用例名称', max_length=200)  # 测试用例名称
    web_test_step = models.CharField('测试步骤', max_length=200)  # 测试步骤
    web_test_objname = models.CharField('测试对象名称描述', max_length=200)  # 测试对象名称描述
    web_find_method = models.CharField('定位方式', max_length=200)  # 定位方式
    web_ev_element = models.CharField('控件元素', max_length=800)  # 控件元素
    web_opt_method = models.CharField('操作方法', max_length=200)  # 操作方法
    web_test_date = models.CharField('测试数据', max_length=200, null=True)  # 测试数据,临时增加字段时要设置可为空
    web_assert_data = models.CharField('校验数据', max_length=200)  # 校验数据
    web_test_result = models.BooleanField('测试结果')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    def __str__(self):
        return self.web_test_step
