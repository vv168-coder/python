import random
from django import forms
import re



class SendSmsCodeForm(forms.Form):
    #发送验证表单
    phone_num=forms.CharField(label='手机号码',required=True,error_messages={'required':'输入手机号'})
    def clean_phone_num(self):
        #验证是否为手机号码
        phone_num=self.cleaned_data['phone_num']
        pattern=r'^1[0-9]{10}$'
        if not re.search(pattern,phone_num):
            raise forms.ValidationError('手机号码不正确',code='invalid_phone',params=(phone_num,))
        return phone_num
    def send_sms_code(self):
        sms_code=random.randint(100001,999999)
        phone_num=self.cleaned_data.get('phone_num',None)
        try:
            #将验证码放入radis中
            # key='sms_code_{}'.format(phone_num)
            timeout=5*60

            #将验证码存放至radis中
            # cache.set(key,sms_code,timeout=timeout)
            return{
                'phone_num':phone_num,
                'sms_code':sms_code,
                'timeout':timeout
            }
        except Exception as e:
            print(e)
            return  None