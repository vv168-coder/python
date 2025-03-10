import json

from django.contrib.auth import logout
from django import http
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from accounts import serializers
from accounts.forms import LoginForm, RegisterForm
from utils.response import BadRequestJsonResponse, MethodNotAllJsonResponse, UnauthorizedJsonResponse, \
    ServerErrorJsonResponse


# 做逻辑处理
# Create your views here.

# request 是前端发起的请求，会整合成一个数据包（自己编的）
def user_login(request):
    #用户登录
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.do_login(request)
            print('表单验证通过')
            return redirect('/accounts/user/info/')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request,'user_login.html',{'form':form})

def user_info(request):
    # 用户信息
    print(request.user)
    return render(request, 'user_info.html')

def user_logout(request):
    # 退出登录
    logout(request)
    return redirect('/accounts/user/info/')


# 前后端分离异步提交登录
def user_api_login(request):
#     确定请求方式
    if request.method == 'POST':
#         表单验证
        form = LoginForm(request.POST)
#         通过验证
        if form.is_valid():
            #           返回内容是登陆用户的信息
            user = form.do_login(request)
#             获取用户的详细信息
            profile = user.profile
#             合成返回数据
            data={
                'user':serializers.UserSerializer(user).to_dict(),
                'profile':serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)
        else:
#            没有通过表单验证，返回错误信息
            err = json.load(form.errors.as_json())
            return BadRequestJsonResponse(err)
    else:
        return MethodNotAllJsonResponse()

def user_api_logout(request):
    logout(request)
    return http.HttpResponse(status=201)


class UserDetailView(View):
    #     用户详情接口
    def get(self, request):
        # 获取用户信息
        user=request.user
        # 判断用户状态是登录还是未登录
        if not user.is_authenticated:
            # 未登录状态返回401状态码
            return UnauthorizedJsonResponse()
        else:
            # 返回详细信息
            profile = user.profile
            data = {
                'user':serializers.UserSerializer(user).to_dict(),
                'profile':serializers.UserProfileSerializer(profile).to_dict()
            }
            return http.JsonResponse(data)# 向客户端的浏览器中响应数据


class UserRegisterView(FormView):
    # 用户注册接口
    form_class = RegisterForm # 表单验证类
    http_method_names = ['post']

    def form_valid(self, form):
        # 验证通过
        result = form.de_register(request = self.request)
        #调用注册函数，完成注册步骤
        if result is not None:
            user,profile = result
            # 合成响应数据
            data = {
                'user':serializers.UserSerializer(user).to_dict(),
                'profile':serializers.UserProfileSerializer(profile).to_dict()
            }
            # 响应数据
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)




























