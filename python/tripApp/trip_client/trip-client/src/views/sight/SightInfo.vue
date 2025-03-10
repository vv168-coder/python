<script setup>

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
const sightInfo = ref({})

const getSightInfo = () => {
    const url = SightApis.sightInfoUrl.replace('#{id}',route.params.id)
    ajax.get(url).then(({data})=>{
        sightInfo.value = data
})
}

onMounted(() => {
    getSightInfo()        
})


</script>


<template>
    <!-- 景点评论 -->
    <div class="page-sight-info">
        <van-nav-bar left-text="返回" title="景点介绍" left-arrow @click-left="goBack"></van-nav-bar>
        <van-panel title="入园参考">
            <div v-html="sightInfo.entry_explain"></div>
        </van-panel>
        <van-panel title="特色玩法">
            <div v-html="sightInfo.play_way"></div>
        </van-panel>
        <van-panel title="温馨提示">
            <div v-html="sightInfo.tips"></div>
        </van-panel>
        <van-panel title="交通到达">
            <div v-html="sightInfo.traffic"></div>
        </van-panel>

        
        <div class="sight-info">
            
        
        </div>
    </div>
</template>


<style scoped>
/* 页面布局样式 */
.page-sight-info {
  padding: 16px;
  background-color: #f5f5f5;
}

/* 导航栏样式 */
.van-nav-bar {
  background-color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

/* 面板样式 */
.van-panel {
  margin-bottom: 16px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

.van-panel__header {
  padding: 16px;
  font-size: 18px;
  font-weight: bold;
  color: #333333;
  background-color: #f9f9f9;
}

.van-panel__content {
  padding: 16px;
}

/* 内容区域样式 */
.sight-info {
  margin-top: 16px;
  background-color: #ffffff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 文本内容样式 */
div[v-html] {
  color: #666666;
  line-height: 1.6;
}

div[v-html] p {
  margin: 0 0 1em;
}

div[v-html] h1, div[v-html] h2, div[v-html] h3 {
  color: #333333;
  margin: 1em 0 0.5em;
}

div[v-html] img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}
</style>