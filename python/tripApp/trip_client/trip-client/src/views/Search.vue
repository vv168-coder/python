<script setup>
import TripFooter from "@/components/common/Footer.vue";
import SightItem from "@/components/common/ListSight.vue";
import { ref, onMounted } from 'vue'

// 向服务端请求数据，需要两个工具，ajax,api
import { ajax } from "@/utils/ajax";
import { SightApis } from "@/utils/apis";
import { showToast } from "vant";
import { useRoute, useRouter } from "vue-router";
import { getContainingBlock } from "vant/lib/utils";

const route = useRoute();
const router = useRouter();

//景点名称
const sightName = ref('')
//景点列表
const dataList = ref([])
//总记录
const totalItem = ref(0)
//当前页码
const currentPage = ref(1)
//每页数据大小
const pageSize = ref(4)
//搜索函数
const onSearch = () => {
    // console.log('onSearch')
    if (!sightName.value) {
        //判断搜索框中是否输入数据，如果没有数据则提示请输入数据
        showToast('请输入景点名称')

        return
    }
    // console.log('搜索',sightName.value)
    dataList.value = []
    currentPage.value = 1
    // 执行查询
    getDataList()

}

// 访问服务端接口获取数据

const getDataList = () => {
    ajax.get(SightApis.sightListUrl, {
        params: {
            name: sightName.value,
            page: currentPage.value,
            limit: pageSize.value

        }
    }).then(({ data: { meta, objects } }) => {
        dataList.value = objects
        totalItem.value = meta.total_count
    })
}

const clear = () =>{
    dataList.value = []
    currentPage.value = 1
    // 执行查询
    getDataList()
}

const pageCange = (page) => {
    getDataList()
}

const isHot = ref('')
const isTop = ref('')

onMounted(() => {
    isHot.value = route.query.isHot
    isTop.value = route.query.isTop

    getDataList()
})

const goback = () => {
    router.go(-1)
}
</script>

<template>
    <div class="page-search">
        <!-- 标题 -->
        <van-nav-bar title="搜索景点" left-text="返回" @click="goback" v-if="isHot || isTop"></van-nav-bar>
        <van-nav-bar title="搜索景点" v-else></van-nav-bar>
        <!-- 搜素框 -->
        <van-search v-model="sightName" 
        show-action label="景点" 
        placeholder="请输入景点名称" 
        @clear="clear"
        @search="onSearch">
            <template #action>
                <div @click="onSearch">搜索</div>
            </template>
        </van-search>
        <!-- 判断显示热门景点还是精选景点 -->
         <h2 v-if="isHot">热门推荐</h2>
         <h2 v-if="isTop">精选推荐</h2>
        <!-- 景点列表 -->
        <div class="sights-list">
            <SightItem v-for="item in dataList" :key="item.id" :item="item"></SightItem>
        </div>
        <!-- 分页 -->
        <van-pagination v-model="currentPage" 
        :total-items="totalItem" 
        :items-per-page="pageSize" 
        @change="pageCange">

        </van-pagination>
        <!-- 底部导航 -->
        <TripFooter v-if="!(isHot || isTop)"></TripFooter>
    </div>
</template>

<style lang="less">
    .page-search {
        padding-bottom: 60px;
    }

</style>