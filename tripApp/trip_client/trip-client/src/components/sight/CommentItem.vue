<script setup>
import { ref,defineProps,computed } from 'vue'   
// 获取父级组件传递的数据,使用defineProps可以接收父级组件传递的数据
const props = defineProps({
    "item":Object
})

const imagesUrls = computed(()=>{
    // 获取服务端返回的评论图片列表，并复制给map集合，病区返回该集合
    return props.item.images.map(i=>i.img)
})
// const rate = ref(3.5)
// const images = [
//     'https://fastly.jsdelivr.net/npm/@vant/assets/apple-1.jpeg',
//     'https://fastly.jsdelivr.net/npm/@vant/assets/apple-2.jpeg',
// ]

const show = ref(false)
const index = ref(0)
const onChange = (index) => {
    index.value=index
}

</script>

<template>
    <div class="comment-item-box">
        <div class="cmt-header">
            <div class="rate">
                <van-rate v-model="item.score" readonly void-icon="star" void-color="#eee"/>
            </div>
            <div class="user">
                {{item.user.nickname || '匿名用户'}} {{item.created_at}}
            </div>
        </div>
        <div class="cmt-content">
            <!-- <p>
                赵微暴富 有钱 有车 有房 有存款<br> 
                赵微暴富 有钱 有车 有房 有存款 <br> 
                赵微暴富 有钱 有车 有房 有存款 <br> 
                赵微暴富 有钱 有车 有房 有存款 <br> 
                赵微暴富 有钱 有车 有房 有存款 
            </p> -->

            {{ item.content }}
        </div>
        <div class="cmt-imgs">
            <van-image width="100" height="100" 
                v-for="(image,index) in item.images" :key="index" 
                :src="image.img" />
        </div>
        <van-image-preview :images="imagesUrls" :show="show" @change="onChange">
            <template v-slot:index>第{{ index+1 }}</template>

        </van-image-preview>
    </div>
</template>


<style lang="less">
.comment-item-box{
    padding:5px 10px;
    border-bottom:1px solid #f6f6f6;
    margin-bottom:10px;
    .cmt-header{
        display: flex;
        .user{
            font-size: 12px;

        }
    }
    .cmt-content{
        color:#616161;
        padding: 5px 0;
        text-align: left;
        font-size: 12px;
        line-height: 2.0;
    }
    .cmt-imgs{
        padding: 5px;
        text-align: left;
        margin-right: 5px;
    }



}

</style>