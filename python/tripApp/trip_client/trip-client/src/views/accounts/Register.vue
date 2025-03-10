<script setup>
// 准备工具

import Copyright from '@/components/common/Copyright.vue';
import SendSmsCode from '@/components/common/SendSmsCode.vue';
import { ref, toRef } from 'vue'
import { useRoute, useRouter } from 'vue-router';

import { ajax } from '@/utils/ajax';
// 导入接口地址
import { AccountsApis } from '@/utils/apis';
import { showToast } from 'vant'


const route = useRoute();
const router = useRouter();

// 准备数据
// 用户名验证
const ruleName = ref([{
    required: true,
    message: '请输入用户名',
}, {
    pattern: /1\d{10}/,
    message: '请输入正确的手机号',
}])

const form = ref({
    username: '',
    nickname: '',
    sms_code: '',
    password: '',
    passwordRepeat: '',
})

const username = ref('')
// 密码验证
const rulePassword = ref([
    {
        required: true,
        message: '请输入密码'
    },
    {
        validator: () => form.value.password === form.value.passwordRepeat,
        message: '两次密码输入不一致'
    }
])

const goBack = () => {
    router.go(-1);
}

const onSubmit = () => {
    // 提交表单
    // 1、调用接口
    ajax.post(AccountsApis.registerUrl,{
      username: form.value.username,
      nickname: form.value.nickname,
      password: form.value.password,
      sms_code: form.value.sms_code,
    }).then(({data})=>{
       // 2、提示用户
       showToast('注册成功,请登录')

       // 跳转到个人中心页面
       router.push({ name: 'AccountLogin' })

    })
   
    
}


// 手机号变化
const refSms = ref({})
const onPhoneChange = () => {
    refSms.value.reset()
}

// 提交

</script>

<template>
    <div class="page-accounts-register">
        <!-- 导航条 -->
        <van-nav-bar titile="注册" left-text="返回" left-arrow @click-left="goBack"></van-nav-bar>
        <!-- 表单 -->
        <van-form @submit="onSubmit">
            <!-- 文本框 -->
            <van-field v-model="form.username" label="手机号码" placeholder="手机号码" maxlength="11" :rules="ruleName"
                clearable @input="onPhoneChange"></van-field>
            <van-field v-model="form.sms_code" center clearable label="短信验证码" placeholder="请输入短信验证码"
                :rules="[{ required: true, message: '请输入短信验证码' }]">

                <template #button>
                    <!-- ref竖向绑定，可以在脚本端直接使用refSms.$el获取组件实例 -->
                    <SendSmsCode ref="refSms" :phoneNum="form.username" />
                </template>
            </van-field>
            <van-field v-model="form.nickname" label="用户昵称" placeholder="用户昵称" maxlength="32"
                :rules="[{ required: true, message: '请输入用户昵称' }]" clearable></van-field>
            <van-field v-model="form.password" label="密码" placeholder="密码"
                :rules="[{ required: true, message: '请输入密码' }]" clearable></van-field>
            <van-field v-model="form.passwordRepeat" label="确认密码" placeholder="确认密码" :rules="rulePassword" clearable>
            </van-field>
            <!-- 提交按钮 -->
            <div style="margin:16px">
                <van-button round block native-type="submit" type="info">注册</van-button>
            </div>
        </van-form>

        <!-- 文字提示 -->
        <!-- 文字提示 -->
        <div class="tips">
            登录表示同意<a href="#">用户使用协议</a><a href="#">隐私条款</a>
        </div>
        <div class="tips">
            已有账户？<RouterLink :to="{ name: 'AccountLogin' }">点击登录</RouterLink>
        </div>

        <!-- 版权信息 -->
        <Copyright></Copyright>

    </div>


</template>
<style scoped>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5f5;
}

.page-accounts-register {
  padding: 16px;
  max-width: 400px;
  margin: 0 auto;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.van-nav-bar {
  background-color: #ffffff;
  border-bottom: 1px solid #eaeaeaea;
}

.van-form {
  margin-top: 16px;
  background-color: #ffffff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.van-field {
  margin-bottom: 16px;
}

.van-button {
  width: 100%;
  padding: 12px;
  background-color: #4CAF50;
  color: #ffffff;
  border-radius: 4px;
  font-size: 16px;
}

.van-button:hover {
  background-color: #45a145;
}

.tips, .tips {
  font-size: 14px;
  color: #888888;
  text-align: center;
  margin-top: 16px;
}

.tips a, .tips a {
  color: #ff4d4f;
  text-decoration: none;
}

.tips a:hover, .tips a:hover {
  text-decoration: underline;
}

.Copyright {
  margin-top: 16px;
  text-align: center;
  color: #999;
  font-size: 12px;
}
</style>