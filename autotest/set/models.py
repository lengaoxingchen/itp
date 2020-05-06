from django.db import models


# Create your models here.

class Set(models.Model):
    set_name = models.CharField('设置名称', max_length=64)  # 设置名称
    set_value = models.CharField('设置值', max_length=200)  # 设置值

    class Meta:
        # 定义在管理后台显示的名称
        verbose_name = '系统设置'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = '系统设置'

    def __str__(self):
        return self.set_name
