from django.db import models


class CommonModel(models.Model):
    # 数据模型公共类
    is_valid = models.BooleanField('是否有效',default=True)
    created_at = models.DateTimeField('创建时间',auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True #此步必不可少，不然就会创建表