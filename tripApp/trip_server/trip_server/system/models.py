from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import User
from utils.models import CommonModel


# Create your models here.
#数据库中表的映射类，根据该文件构建及操作数据库
class Slider(CommonModel):

    # 轮播图
    name = models.CharField('姓名',max_length=32)
    desc = models.CharField('描述',max_length=100,null=True,blank=True)
    type = models.SmallIntegerField('展现的文职',default=10)
    img = models.ImageField('图片地址',max_length=255,upload_to='%Y%m/slider')
    reorder = models.SmallIntegerField('排序字段',default=0,help_text='数字越大越靠前')
    start_time = models.DateTimeField('生效开始时间',null=True,blank=True)
    end_time = models.DateTimeField('生效结束时间', null=True, blank=True)
    target_url = models.CharField('跳转的地址',max_length=255,null=True,blank=True)
    # is_valid = models.BooleanField('是否有效',default=True)
    # created_at = models.DateTimeField('创建时间',auto_now_add=True)
    # updated_at = models.DateTimeField('修改时间', auto_now=True)


    class Meta:
        db_table = 'system_sliders'
        ordering = ['-reorder']#默认排序规则


class ImageRelated(CommonModel):
    # 图片资源
    # 图片地址列用于记录图片所在地址
    img = models.ImageField('图片',upload_to='%Y%m/file/',max_length=256)
    # 图片说明（描述）列用于记录图片简介、名称等信息
    summary = models.CharField('图片说明',max_length=32,null=True,blank=True)
    # 用户id(主键)列，参数1 用户数据源可以将用户id传入到该属性中
    # 参数2：级联关系，主键删除后，外建置空
    # 参数3：关联名字
    # 参数4：识别名
    # 参数5 允许为空null
    user = models.ForeignKey(User,on_delete=models.SET(None),related_name='upload_image',verbose_name='上传的用户',null=True)
    # 类型适配列，如两个表没有配置主外键关系，还需要实现主外键关联查询，
    # 传统的处理方式，构建一张字典表，将主外关系建立起来
    # 在django中提供构建主外键关系的策略，使用django_content_type实现改该字典表功能
    # ContentType特征每构建一个新数据源会在该表中进行注册，用于之后的主外关系，由django框架维护
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    # 关联名称标识
    object_id = models.IntegerField('关联模型')
    # 配置主外关联关系，如向system_image_related表中添加数据时
    # 需要明确Content_id对应django_content_type表中哪一个id值
    content_object = GenericForeignKey('content_type','object_id')

    class Meta:
        db_table = 'system_image_related'

