<script setup>
import CommentItem from '@/components/sight/CommentItem.vue';
import {ref,onMounted,computed} from 'vue'
import {useRoute,useRouter} from 'vue-router'//用于控制页面跳转工具
import {ajax} from '@/utils/ajax'//用于发送请求的工具
import { SightApis } from '@/utils/apis';

const route = useRoute()//获取路由参数
const router = useRouter()//获取路由实例

const goBack = () => {
    router.go(-1)//跳转至上一页
}

// 获取景点详情
// {} 用于表示对象，python字典，由于服务端响应的数据是对象的格式因此使用{}承载
const sightDetail = ref({})
const getSightDetail = () => {
    // 发送请求获取景点详情
    // route.params.id 获取地址栏携带的id值
    const url = SightApis.sightDetailUrl.replace('#{id}',route.params.id)
    ajax.get(url).then(({data})=>{
        sightDetail.value = data
    })
}

// 获取景点地址
// computed计算属性,用于数据处理的函数如何返回数据进行格式化
const fullArea = computed(()=>{

    let area = sightDetail.value.province+sightDetail.value.city
    if(sightDetail.value.area){
        area += sightDetail.value.area
    }
    if(sightDetail.value.town){
        area += sightDetail.value.town

    }
    return area
})

// 获取景点门票
const ticketList = ref([])
const getTicketList = () => {
    // 发送请求获取门票列表
    const url = SightApis.ticketListUrl.replace('#{id}',route.params.id)
    ajax.get(url).then(({data})=>{
        ticketList.value = data.objects
    })
}
// 获取景点评论
const commentList = ref([])
const getCommentList = () => {
    const url = SightApis.sightCommentUrl.replace('#{id}',route.params.id)
    ajax.get(url).then(({data})=>{
        commentList.value = data.objects
    })
}

onMounted(()=>{
    getSightDetail()
    getTicketList()
    getCommentList()
})

// const getSightInfo = () => {
//     // 跳转至景点介绍页面
//     router.push({name:'SightList',params:{id:route.params.id}})
// }
</script>

<template>
    <!-- 景点详情 -->
    <div class="page-sight-detail">
        <!-- 页面头部 -->
         <van-nav-bar left-text='返回' left-arrow fixed @click-left="goBack"></van-nav-bar>
        <!-- 景点大图 -->
         <div class="page-banner">
            <van-image :src="sightDetail.img" width="100%" height="100%"></van-image>
            <div class="tips">
                <RouterLink class="pic-sts" :to="{name:'SightList'}"></RouterLink>
                    <van-icon name="video-o"></van-icon>
                    <div class="title">{{sightDetail.name}}</div>
            </div>       
        </div>
        <!-- 景点介绍 -->
         <div class="sight-info">
            <div class="left">
                <RouterLink :to="{name:'SightAddComment',params:{id:route.params.id}}" class="info-title" >
                    <strong>{{sightDetail.score}}分</strong>
                    <small>很棒</small>
                </RouterLink>
                <div cass="info-tips">
                    {{ sightDetail.comment_count }} 评论
                </div>
                <van-icon class="arrow"></van-icon>
            </div>
            <div class="right">
                <!-- div块级元素，独占一行 -->
                <div class="info-title">
                    <span>
                        <RouterLink :to="{name:'SightInfo',params:{id:route.params.id}}">景点介绍</RouterLink>
                    </span>
                </div>
                <div class="info-tips">
                    开放时间、注意
                </div>
                <van-icon class="arrow"></van-icon>
            </div>
         </div>
        <!-- 地址信息 -->
         <!-- fullArea 计算属性，默认可以数据联动，普通属性需要加冒号 -->
        <van-cell :title=fullArea icon="location-o" is-link :title-style="{'text-align':'left'}">
            <template #right-icon>
                <van-icon name="arrow"/>
            </template>
        </van-cell>
        <!-- 门票列表 -->
         <div class="sight-ticket">
            <van-cell title="门票" icon="bookmark-o" title-style="text-align:left"/>
            <div class="ticket-item" v-for="item in ticketList" :key="item.id">
                <div class="left">
                    <div class="title">{{item.name}}</div>
                    <div class="tips">
                        <van-icon name="clock-o"/>
                        <span>{{item.desc}}</span>
                    </div>
                    <div class="tags">
                        <van-tag make type="primary">标签1</van-tag>
                    </div>
                </div>
                <div class="right">
                    <div class="price">
                        <span>¥</span>
                        <strong>{{item.price*item.discount/10}}</strong>
                    </div>
                    <RouterLink to="/#">
                        <van-button type="warning" size="small">预定</van-button>
                    </RouterLink>
                </div>
            </div>
         </div>
        <!-- 用户评价 -->
        <div class="sight-comment">
            <van-cell title="热门评论" icon="comment-o" title-style="{'text-align':'left'}"/>
            <CommentItem v-for="item in commentList" :key="item.pk" :item="item"/>
            <RouterLink :to="{name:'SightComment',params:{id:route.params.id}}" class="link-more">查看更多</RouterLink>
        
        </div>
        <!-- 地图位置 -->
    </div>
</template>

<style lang="less">
.van-nav-bar {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.page-sight-detail{
    .sight-banner {
        position: relative;

        .tips {
            position: absolute;
            left: 10px;
            bottom: 10px;
            font-size: 16px;
            color: #fff;

            .pic-sts {
                color: #fff;
                border-radius: 5px;
                font-size: 14px;
                background-color: rgba(0, 0, 0, 0.5);
            }
        }
    }

    .sight-info {
        display: flex;
        background-color: #fff;
        border-bottom: 1px solid #eee;
        &>div {
            //同级下的所有div
            flex: 1;
            position: relative;
        }
        .right {
            border-left: 1px solid #f6f6f6;
        }
        .info-title {
            text-align: left;
            padding: 5px 10px;
            strong {
                color: orange;
            }
        }
        .info-tips {
            color: #999;
            font-size: 12px;
            text-align: left;
            padding: 5px 10px;

        }
        .van-icon {
            position: absolute;
            right: 5px;
            top: 10px;
        }
        
    }
    .sight-ticket {
            margin-top: 10px;
            background-color: #fff;
            .ticket-item {
                display: flex;
                border-bottom: 1px solid #f6f6f6;
                padding-bottom: 10px;
                .left {
                    flex: 1;
                    text-align: left;
                    padding: 5px 10px;
                    .title {
                        padding: 5px 0;
                    }
                    .tips {
                        font-size: 12px
                    }
                }
                .right {
                    flex: 1;
                    width: 100px;
                    .price {
                        color: orange;
                        strong {
                            font-size: 20px;
                        }
                    }
                }
            }
    }
    .sight-comment{
        margin-top: 10px;
        background-color: #fff;
    }
    .link-more{
        display: block;
        color: #666;
        padding: 10px;
        text-align: center;
    }
}


</style>