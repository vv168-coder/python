<script setup>
import { ref } from 'vue'
const active = ref()

</script>

<template>
    <div>
        <van-tabbar v-model="active">
            <van-tabbar-item icon="wap-home-o" name="home" :to="{name:'home'}">首页</van-tabbar-item>
            <van-tabbar-item icon="search" name="search" :to="{ name: 'Search' }">搜索</van-tabbar-item>
            <van-tabbar-item icon="user-o" name="mine" :to="{ name: 'Mine' }">我的</van-tabbar-item>
        </van-tabbar>
    </div>
</template>