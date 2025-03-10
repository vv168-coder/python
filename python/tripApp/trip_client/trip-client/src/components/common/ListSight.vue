<script>
    export default{
        props: ['item']
    }
</script>

<template>
    <router-link :to = "{name:'SightDetail',params:{id:item.id}}" class="sight-item" >
        <img :src="item.main_img" alt="">
        <div class="right">
            <h5>{{item.name}}</h5>
            <van-rate v-model="item.score" readonly="" allow-half/>
            <div class="tips">{{ item.comment_count }}人点评 | 100%满意 </div>
            <div class="tips light">{{item.province}}-{{ item.city }}</div>
            <div class="line-price">¥{{ item.min_price }}</div>
        </div>
    </router-link>
</template>

<style lang="less">
.sight-item{
    display: flex;
    margin-top: 10px;
    border-bottom: 1px solid #f6f6f6;

    img{     
        width: 100px;
        height: 100px;
    
    }
    .right{
        text-align: left;
        flex-grow: 1;//布局填充，默认值0保留原大小，1扩大填充
       justify-content: left;//全部居左，小星星
        padding-left: 5px;
        margin-left: 5px;
        position: relative;//父级动，跟着动
    }
    h5{
        color:#212121;
        font-size: 14px;
        padding:5px;
        margin: 0px;
    }
    .line-price{
        color: orange;
        font-size: 16px;   
        position:absolute;
        right: 10px;
        top: 20px;
        display: inline-block;
        font-weight: bold;                
    }
    .tips{
        font-size: 12px;
        color: #666;
        &.light{//当前级别的所有元素
            color: #999;
        }
    }
}
</style>