from product.models import Product
from django.db import models


# Create your models here.

class ApiTest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关键产品ID,其中product是应用名,
    # Product是product应用的表名
    apitest_name = models.CharField('流程接口名称', max_length=64)  # 流程接口测试场景
    apitest_desc = models.CharField('描述', max_length=64, null=True)  # 流程接口描述
    apitester = models.CharField('测试负责人', max_length=16)  # 执行人
    apitest_result = models.BooleanField('测试结果')  # 流程接口测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间,自动获取当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitest_name


class ApiStep(models.Model):
    ApiTest = models.ForeignKey('ApiTest', on_delete=models.CASCADE)  # 关键接口id
    api_step = models.CharField('测试步骤', max_length=100, null=True)  # 接口步骤
    api_name = models.CharField('接口名称', max_length=100)  # 接口标题
    api_url = models.CharField('url地址', max_length=200)  # 接口地址
    api_param_value = models.CharField('请求参数和值', max_length=800)  # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    api_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200,
                                  null=True)  # 请求方法
    api_result = models.CharField('预期结果', max_length=200)  # 预期结果
    api_response = models.CharField('响应数据', max_length=5000, null=True)  # 响应数据
    api_status = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间,自动获取当前时间

    def __str__(self):
        return self.api_step
