from django.db import models
from product.models import Product


# Create your models here.

class Bug(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    bug_name = models.CharField('bug名称', max_length=64)  # bug名称
    bug_detail = models.CharField('bug详情', max_length=200)  # bug详情
    BUG_STATUS = (('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭'), ('重新打开', '重新打开'))
    bug_status = models.CharField(verbose_name='解决状态', choices=BUG_STATUS, default='激活', max_length=200,
                                  null=True)  # bug解决状态
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    bug_level = models.CharField(verbose_name='严重程度', choices=BUG_LEVEL, default='3', max_length=200,
                                 null=True)  # bug严重程度
    bug_creater = models.CharField('bug创建人', max_length=200)  # 创建人
    bug_assign = models.CharField('bug分配人', max_length=200)  # bug 分配给谁
    create_time = models.DateTimeField('创建时间', auto_now=True)  # bug 创建时间

    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'

    def __str__(self):
        return self.bug_name
