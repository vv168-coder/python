from django import http
import json

from django.views.generic import FormView

from system.forms import SendSmsCodeForm
from system.models import Slider
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


# Create your views here.
#创建视图函数用户返回轮播数据列表
def slider_list(request):
    #规范响应数据结构
    data = {
        'meta':{
            #返回的协议404/401
        },
        'objects':[]
    }
    queryset = Slider.objects.filter(is_valid=True)#对数据源（数据库里的数据）进行过滤，相当于在sql语句中加where条件
    #对结果集进行遍历，将数据封装至objects中
    for item in queryset:
        data['objects'].append({
            'id':item.id,
            'img_url':item.img.url,
            'target_url':item.target_url,
            'name':item.name,
        })
    #用于网络传输的标准的数据格式，返回一个json的对象
    return http.JsonResponse(data)


class SmsCodeView(FormView):
    form_class = SendSmsCodeForm
    def form_valid(self, form):
        #生成并获得验证码
        data=form.send_sms_code()
        if data is not None:
            return http.JsonResponse(data,status=201)
        return ServerErrorJsonResponse()
    def form_invalid(self,form):
        #表单未通过验证
        err_list=json.loads(form.errors.as_json())
        print("Form Validation Errors:", err_list)  # 打印错误信息
        return BadRequestJsonResponse(err_list)