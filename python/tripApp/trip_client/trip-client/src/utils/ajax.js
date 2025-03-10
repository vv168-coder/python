import axios from 'axios';
//创建axios对象，并暴露该对象可以被外部访问
//创建对象是对其进行头信息及加载上一次携带的cookie
export const ajax = axios.create({
    headers:{
        source:'h5',
        'Content-Type':'application/x-www-form-urlencoded'
    },
    withCredentials:true,
})




//请求拦截器
//参数1：拦截成功；参数2：拦截异常
//两个参数都传递箭头函数用于数据具体过程
//处理完毕需要放行
// ajax.interceptors.request.use((req)=>{
//     console.log('请求拦截到了')
//     console.log(req.url)
//     return req
// },(err)=>{
//     return Promise.reject(err)//处理异常的函数
// })
//响应拦截器
//参数1：拦截成功；参数2：拦截异常
//两个参数都传递箭头函数用于数据具体过程
//处理完毕需要放行
// ajax.interceptors.response.use((reqs)=>{
//     // console.log('响应拦截到了')
//     return reqs
// },(err)=>{
//     if(err.response.status === 401){
//         window.alert('请重新登录')
//         //跳转到登录页面
//     }
//     return Promise.reject(err)
// })

// 对axios进行全局配置可提升代码的可维护性