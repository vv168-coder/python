from django.contrib.auth.models import AbstractUser
from django.db import models


# 模型 抗拒不匹配
# 如何设计的工程，有什么特点
# Create your models here.
from utils.models import CommonModel

class User(AbstractUser):
    #用户数据模型
    # username = models.CharField('用户名',max_length=50, unique=True)
    # password = models.CharField('密码',max_length=256)
    # nickname = models.CharField('昵称', max_length=32, unique=True)
    # avatar = models.ImageField('头像', null=True,upload_to='avatar/%Y%m')

    nickname = models.CharField('昵称', max_length=32, unique=True)
    avatar = models.ImageField('头像', null=True,upload_to='avatar/%Y%m')

    class Meta:
        db_table = 'account_user'

    def add_login_record(self,**kwargs):
#         写入日志
        self.login_record.create(**kwargs)
    @property
    def avatar_url(self):
        return self.avatar_url if self.avatar else ''

class Profile(models.Model):
    # 用户详细信息
    # 性别
    # 手机号码
    # 年龄
    # 生日
    # 真实姓名
    # 创建常量1表示男，0表示女
    SEX_CHIOCES = {
        (1,'男'),
        (0,'女')
    }

    username = models.CharField('用户名',max_length=64,unique=True,editable=False)
    user = models.OneToOneField(User,related_name = 'profile' ,on_delete=models.CASCADE)
    real_name = models.CharField('真实姓名',max_length=32)
    email =  models.CharField('电子邮件',max_length=128)
    is_email_valid = models.BooleanField('邮箱是否已经验证',default=False)
    phone_no = models.CharField('手机号码',max_length=16,null=True,blank=True)
    is_phone_valid = models.BooleanField('是否已经验证', max_length=16, default=False)
    sex = models.SmallIntegerField('性别',default=1,choices=SEX_CHIOCES)
    age = models.SmallIntegerField('年龄',default=0)


    source = models.CharField('登录的来源',max_length=32,null=True)
    version = models.CharField('版本号',max_length=32,null=True)
    created_at = models.DateTimeField('创建时间',auto_now_add=True)
    updated_at = models.DateTimeField('修改时间',auto_now=True)

    class Meta:
        db_table = 'account_user_profile'


class LoginRecord(models.Model):
    # 用户登录日志
    # 关联用户
    # 登录账号
    # 登录的时间
    # ip
    # 登录的来源
    # 登录的客户端版本号


    user = models.ForeignKey(User,related_name='login_record',on_delete=models.CASCADE)
    username = models.CharField('登录的账号',max_length=64)
    ip = models.CharField(' IP',max_length=32)
    address = models.CharField('地址',max_length=32,null=True,blank=True)
    source = models.CharField('登录的来源',max_length=16,null=True)
    version = models.CharField('登录的版本',max_length=16,null=True)


    created_at = models.DateTimeField('登录时间',auto_now_add=True)



    class Meta:
        db_table = 'account_login_record'