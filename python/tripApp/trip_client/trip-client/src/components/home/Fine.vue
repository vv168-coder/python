<script setup>
import ListSight from '../common/ListSight.vue';
import { ref,onMounted } from 'vue'
import {ajax} from '@/utils/ajax'
import { SightApis } from '@/utils/apis';

// const FineList = ref([
//     {id:1,name:'景点名称',scorse:5,price:98},
//     {id:2,name:'景点名称',scorse:4.5,price:88},
//     {id:3,name:'景点名称',scorse:3,price:78},
//     {id:4,name:'景点名称',scorse:2,price:68},
//     {id:5,name:'景点名称',scorse:1,price:58},
//     {id:6,name:'景点名称',scorse:5,price:98},
// ])


const FineList = ref([])
const getFineList = () => {
    ajax.get(SightApis.sightListUrl,{
        params: {
            is_top:1
    }}).then(({data})=>{
        //对象，value是属性,脚本端掉的就是对象，value是属性
        FineList.value = data.objects
        // console.log(FineList.value)
    })

}

onMounted(() => {
    getFineList()
})
</script>
<template>
    <!-- 精选景点 -->
    <div class="home-fine-box">
        <!-- 顶部导航 -->
        <div class="home-fine-title">
            <van-cell title="精选景点" is-link value="更多" 
            icon="location-o"
            title-style="text-align:reft;"
            :to="{name:'Search',query:{isTop:1}}"/>
        </div>  
        <!-- 精选景点列表 -->
        <div class="box-main">
            <ListSight v-for="item in FineList" :key="item.id" :item="item"/>
        </div>
    </div>

</template>

<style lang="less">
   .home-fine-box{
        padding: 0 10px;
        .van-cell{
            padding: 10px 0;
        }
        //设置景点列表
        .box-main{
            padding-bottom: 50px;
        }
    }

</style>