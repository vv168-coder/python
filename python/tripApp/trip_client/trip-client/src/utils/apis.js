// 用于和服务端进行接口交互的

import sendSmsCode from "@/components/common/SendSmsCode.vue"

//5173转8000触发跨域
const apiHost = '/api'

// 用户相关的接口
const AccountsApis = {
    // 用户注册
    registerUrl:apiHost+"/accounts/user/api/register/",
    // 用户登录
    loginUrl:apiHost+"/accounts/user/api/login/",

}

// 系统相关的接口
const SystemApis = {
    sliderListUrl:apiHost+"/system/slider/list/",
    // 发送验证码
    sendSmsCodeUrl:apiHost+"/system/send/sms/",
}


// 景点相关的接口
const SightApis = {
    // 访问服务端的接口地址
    // 访问景点列表
    sightListUrl:apiHost+"/sight/sight/list/",
    // 访问景点详情
    sightDetailUrl:apiHost+"/sight/sight/detail/#{id}/",
    // 门票列表
    ticketListUrl:apiHost+"/sight/ticket/list/#{id}/",
    // 评论列表
    sightCommentUrl:apiHost+"/sight/comment/list/#{id}/",
    // 景点介绍
    sightInfoUrl:apiHost+"/sight/sight/info/#{id}/",
    //添加评论
    addCommentUrl:apiHost+"/sight/sight/addcomment/#{id}/",
    //添加收藏
}


//对外暴漏
export {
    SystemApis,
    SightApis,
    AccountsApis
}