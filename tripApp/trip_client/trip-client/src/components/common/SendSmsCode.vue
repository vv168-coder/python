<script setup>
import CommentItem from '@/components/sight/CommentItem.vue';
// defineProps用于父子通信的
import {ref,onMounted,computed,defineProps} from 'vue'
import {useRoute,useRouter} from 'vue-router'//用于控制页面跳转工具
import { showToast } from 'vant';
// 导入异步提交工具
import {ajax} from '@/utils/ajax';
// 导入接口地址
import { SystemApis } from '@/utils/apis';

const route = useRoute()//获取路由参数
const router = useRouter()//获取路由实例

const goBack = () => {
    router.go(-1)//跳转至上一页
}

const props = defineProps({
    phoneNum:String
})
// 存放验证信息
const isSmsSend = ref(false)
const sendBtnText = ref('发送验证码')
const timer = ref(null)
const counter = ref(60)



// 提示// 清空验证码计时
const reset=()=>{
    isSmsSend.value = false
    sendBtnText.value = '发送验证码'
    if(timer.value){
        clearInterval(timer.value)//停止回到海曙
        counter.value = 60
        timer.value = null
}
}
// 倒计时
const countDown = () => {
    //回调函数
    timer.value = setInterval(() => {
        sendBtnText.value=`(${counter.value}秒)后重新发送`
        counter.value--
        if(counter.value<0){
            reset()
            }
    },1000)

}
// 发送验证码
const sendSmsCode=() => {
    //判断手机号是否输入
    if(!props.phoneNum){
        showToast('请输入手机号')
        return false
    }
    //调用接口，发送短信
    ajax.post(SystemApis.sendSmsCodeUrl,{
        phone_num:props.phoneNum
    }).then(({data})=>{
        //提示验证码已经发送
        let message=`验证码为:${data.sms_code},${data.timeout/60}分钟内有效`
        showToast(message)
        //倒计时
        isSmsSend.value=true
        countDown()
    }).catch((err)=>{
        //如果产生异常，提示发送失败
        isSmsSend.value=false
        sendBtnText.value='发送验证码'
        console.log(err)
        showToast('发送失败')
    })
}
// 向父级暴漏的接口
defineExpose({
    reset
})
</script>

<template>
<!-- 短信验证码发送相关的逻辑 -->
 <van-button size="small" type="primary"
 @click.prevent="sendSmsCode()" :disabled="isSmsSend">
 {{sendBtnText}}
 </van-button>
</template>
