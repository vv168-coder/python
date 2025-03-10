<!-- 用于处理数据及函数的 -->
<script setup>
// import axios from 'axios';//导入依赖工具包
import { onMounted } from 'vue';//导入onMounted工具
import {ajax} from '@/utils/ajax' 
import { ref } from 'vue';//导入响应式变量
import Banner from '@/components/home/Banner.vue'
import Hot from '@/components/home/Hot.vue'
import Fine from '@/components/home/Fine.vue';
import TripFooter from '@/components/common/Footer.vue';

// import Button from 'vant/lib/button';//导入按钮组件
// import 'vant/lib/button/style'
//页面加载前执行，也称为钩子函数或生命周期函数
// ()=> {}箭头函数，用于执行具体内容,es6提供的
// onMounted(()=> {
// //   //axios用于异步提交的工具，可以向服务器发起请求，获取服务端响应的数据
// //   //get()以get提交方式向服务器发起请求，参数是请求的目标地址
// //   //then()用于处理服务器响应的数据，获取响应信息，将响应的数据传递给resp
// //   //=>{}箭头函数用于处理响应数据的函数
// //   //console.log()用于打印响应数据到控制台
//   ajax.get("http://localhost:8000/sight/sight/list/").then(resp=>{
//     console.log('响应返回的数据',resp);
//   }).catch(err=>{
//     console.log('请求失败',err);
//   })
// }) 
//注意：直接通过当前工程访问目标会触发跨域问题，需要进一步的配置
//什么是跨域？通过当前站点访问领一个站点为跨域



</script>
<!-- onMounted() 生命周期函数，在页面元素加载前就执行，浏览器打开元素未显示，则执行该程序 -->

<!-- 用于显示页面内容 -->
<template>
  <!-- 轮播图 -->  
  <Banner></Banner>
  <Hot></Hot>
  <!-- 本周推荐 -->
  <!-- 精选景点 -->
  <Fine></Fine>
  <!-- 底部导航 -->
  <TripFooter></TripFooter>
  <!-- <TripFooter></TripFooter> -->
</template>
<!-- 用于美化页面的 -->
<style lang="less">

</style>       