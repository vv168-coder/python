from django import forms
import re
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from accounts.models import User, Profile


class LoginForm(forms.Form):
    # 登录表单
    username = forms.CharField(label='用户名',required=False,help_text='使用帮助',initial='admin')
    password = forms.CharField(label='密码',max_length=200,min_length=6,widget=forms.PasswordInput)

    # 初始化函数，将传入的数据给到父类中处理
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    # 验证用户名的钩子函数
    def clean_username(self):
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern,username):
            raise forms.ValidationError('手机号码%s输入不正确',code='invalid_phone',params= (username,))
        return username

    def clean(self):
        data = super().clean()
        if self.errors:
            return

        # 获取模版中输入的用户名密码
        username = data.get('username',None)
        password = data.get('password',None)
        # 验证用户名
        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            if not user.is_active:
                raise forms.ValidationError('该用户已经被禁用')
        self.user = user
        return data

    # 登录函数
    def do_login(self,request):
        user = self.user
        # 调用登录
        login(request, user)
        # 修改登录时间
        user.last_login = now()
        user.save()
        return user

class RegisterForm(forms.Form):
    # 用户名
    username = forms.CharField(label='手机号码',max_length=16,required=True,error_messages={
        'required':'请输入手机号'
    })
    # 密码
    password = forms.CharField(label='密码',max_length=128,required=True,error_messages={
        'required':'请输入密码'
    })
    nickname = forms.CharField(label='昵称',max_length=16,required=True,error_messages={
        'required':'请输入昵称'
    })
    sms_code = forms.CharField(label='验证码',max_length=6,required=True,error_messages={
        'required':'请输入验证码'
    })


    def clean_username(self):
        #验证用户名
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern,username):
            raise forms.ValidationError('手机号码%s输入不正确',code='invalid_phone',params= (username,))

        # 利用数据模型对手机内容进行验证
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('手机号码已被使用')
        return username

    def clean_nickname(self):
        #验证昵称
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('昵称已被使用')
        return nickname


    def clean(self):
        data = super().clean()
        if self.errors:
            return
        phone_num = self.cleaned_data.get('username',None)
        sms_code = self.cleaned_data.get('sms_code',None)

        # 注册验证码存入redis中
        return data

    def de_register(self,request):
        # 执行注册
        data = self.cleaned_data
        version = request.headers.get('version','')
        source = request.headers.get('source','')

        try:
        # 写入基本信息
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                nickname=data['nickname'],
            )
        # 写入详细信息
        # 2、写入详细信息
            profile = Profile.objects.create(
                user=user,
                username=user.username,
                version=version,
                source=source
            )


        # 登录
            login(request, user)
            user.last_login = now()
        # 保存数据
            user.save()
            # 获得IP地址
            ip = request.META.get('REMOTE_ADDR', '')
            # 4、写入日志
            user.add_login_record(username=user.username, ip=ip, source=source, version=version)
            return user, profile

        # 写入日志



        except Exception as e:
            print(e)
            return None

