<script setup>
import { onMounted,ref } from 'vue';
import { ajax } from '@/utils/ajax';
import { SightApis } from '@/utils/apis';
    // const hotList = ref([
    //     {id:1,img:'/static/home/hot/h1.jpg',name:'景点名称',price:65},
    //     {id:2,img:'/static/home/hot/h2.jpg',name:'景点名称',price:65},
    //     {id:3,img:'/static/home/hot/h3.jpg',name:'景点名称',price:65},
    //     {id:4,img:'/static/home/hot/h4.jpg',name:'景点名称',price:65},
    //     {id:5,img:'/static/home/hot/h5.jpg',name:'景点名称',price:65},
    //     {id:6,img:'/static/home/hot/h6.jpg',name:'景点名称',price:65},
    //     {id:7,img:'/static/home/hot/h7.jpg',name:'景点名称',price:65},
    //     {id:8,img:'/static/home/hot/h8.jpg',name:'景点名称',price:65},
    //     {id:9,img:'/static/home/hot/h9.jpg',name:'景点名称',price:65},
    //     {id:10,img:'/static/home/hot/h10.jpg',name:'景点名称',price:65}
        
    // ]);

const hotList = ref([]);
const getHotList = () => {
    ajax.get(SightApis.sightListUrl,{
        params: {//向目标url发送请求时，附带的参数，
            is_hot: 1,//存在，并不是值等于1
        }
    }).then(({data})=>{
        hotList.value = data.objects;
        // console.log(hotList.value);
    })
}
onMounted(()=>{
    getHotList();
})
</script>
<template>
    <!-- 热门景点 -->
    <div class="home-hot-box">
        <!-- 顶上导航 -->
            <div class="nav">
                <van-cell title="热门推荐" is-link value="全部榜单" 
                icon="/static/home/hot/fire.png"
                title-style="text-align:reft;"
                :to="{name:'Search',query:{isHot:1}}"/>
            </div>
            <div class="box-main">
                <!-- #RouterLink相当于a超链接，通过该标记可以访问路由列表，根据列表访问目标 -->
                <RouterLink class="hot-item"
                v-for="item in hotList" :key='item.id' 
                :to="{name:'SightDetail',params:{id:item.id}}">
                    <div class="img">
                        <span></span>
                        <img :src="item.main_img" alt="">
                    </div>
                    <h5 class="van-ellipsis">{{ item.name }}</h5>
                    <div class="line-price">
                        <span class="price">¥{{ item.min_price }}</span>起
                    </div>
                </RouterLink>

            </div>
        <!-- 景点列表 -->
    </div>
</template>

<style lang="less">
    .home-hot-box{
        padding: 0 10px;//内边距，上下0，左右10px
        //设置顶部导航样式
        .van-cell{
            padding: 10px 0;
        }
        //设置景点列表
        .box-main{
            width: 100%;display: flex;padding-top: 10px;overflow: scroll;
        }
        //热门元素
        .hot-item{
            //flex-direction 决定弹性布局的方向（主轴方向），默认横向
            //column 主轴为垂直方向，起点在上沿
            display: flex;flex-direction: column;
            width: 100px;
            margin-right: 10px;
            padding-bottom: 10px;
        
        //图片
        .img{
           position: relative;//相对定位
           span{
                position: absolute;
                left: 0;
                top: 0;
                display: inline-block;
                width: 42px;
                height: 20px;
                z-index: 10;
           }
           img{
            width: 100px;
            height: 100px;
           }
        }
        h5{
            color: #212121;padding: 2px 0;
            font-size: 12px;
            margin: 0px;
            text-align: center;
            

        }
        .line-price{
            color: #212121;
            font-size: 12px;
            text-align: center;
            .price{
                color: orange;
                font-size: 13px;
            }
        }
        //当前所有的元素节点
        &:nth-child(1) .img span{
            background: url(/static/home/hot/top1.png) no-repeat;
            background-size: 100% auto;
            
        }
        &:nth-child(2) .img span{
            background: url(/static/home/hot/top2.png) no-repeat;
            background-size: 100% auto;
            
        }
        &:nth-child(3) .img span{
            background: url(/static/home/hot/top3.png) no-repeat;
            background-size: 100% auto;
            
        }
    }
}

</style>