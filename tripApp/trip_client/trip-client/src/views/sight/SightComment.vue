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


// 评论列表
const commentList = ref([])

const getCommentList = () => {
    const url = SightApis.sightCommentUrl.replace('#{id}',route.params.id)
    ajax.get(url).then(({data})=>{
        commentList.value = data.objects
})
}

onMounted(() => {
    getCommentList()        
})

</script>


<template>
    <!-- 景点评论 -->
    <div class="page-sight-commment">
        <van-nav-bar left-text="返回" title="景点评论" @click="goBack"></van-nav-bar>
        <div class="sight-comment">
            <CommentItem v-for="item in commentList" :key="item.pk" :item="item"></CommentItem>

        </div>
    </div>
</template>

<style lang="less" >
    .page-sight-commment{
        background-color: white;
    }

</style>