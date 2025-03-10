#该文件用于暴露视图函数的链接地址

from django.urls import path

from system import views
from system.views import SmsCodeView

#配置访问地址列表
urlpatterns = [
    #path配置具体的函数地址，参数一：自定义访问地址。 参数2：函数名称 参数3：连接名字
    path('slider/list/', views.slider_list, name='slider_list'),
    path('send/sms/',SmsCodeView.as_view(),name='send_sms')

]
