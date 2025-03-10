<script setup>
import { ref,onMounted } from 'vue';//获得vue中响应式函数和生命周期函数

import { ajax } from '@/utils/ajax';//获得axios异步提交请求对象
import { SystemApis } from '@/utils/apis';//获得访问目标（轮播图数据）
// // 轮播图数据
// const bannerList = ref([
//   {
//     id:'1',imgUrl:'/static/home/banner/banner1.jpg'
//   },{
//     id:'2',imgUrl:'/static/home/banner/banner2.jpg'
//   },{
//     id:'3',imgUrl:'/static/home/banner/banner3.jpg'
//   }
// ])


const bannerList = ref([]);//轮播图数据,创建列表，用于存放接口返回数据
// 访问接口获取数据
const getBannerList = () => {
  ajax.get(SystemApis.sliderListUrl).then(res => {
    //将获取的轮播图数据给到响应式对象BannerList中
    bannerList.value = res.data.objects;
    // console.log(bannerList.value);//控制台输出响应对象中的数据，测试是否获取到接口返回的数据
  })
}

// 页面加载完成后，执行getBannerList函数，获取轮播图数据
onMounted(() => {
  getBannerList();
})

</script>
<template>
    <div class="home-banner-box">
    <van-swipe class="my-swipe":autoplay='3000' indicator-color="white">
      <van-swipe-item v-for="item in bannerList":key=item.id>
        <img :src=item.img_url alt="">
      </van-swipe-item>
    </van-swipe>
   </div>
</template>

<style lang="less">
  .home-banner-box {
    img{
      width: 100%;
      height: auto;
    }
  }
  
</style>

