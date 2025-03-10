<script setup>
import TripFooter from "@/components/common/Footer.vue";
import {ajax} from '@/utils/ajax'
import {ref} from 'vue'


// const 

</script>

<template>
    <div class="page-mine">
        <!-- 标题栏 -->
        <van-nav-bar title="个人中心" />
        <!-- 用户基本信息 -->
        <div class="user-header">
            <div class="avatar">
                <img src="https://img.yzcdn.cn/vant/user-inactive.png" alt="用户头像" />

            </div>
            <div>
                <p>欢迎您</p>
                <a class="btn-link" href="/account/login">登录</a>
            </div>
        </div>
        <!-- 订单菜单列表 -->
        <van-row>
            <van-col span="6">
                <RouterLink to="/">
                    <van-icon name="records" />
                    <span>全部订单</span>
                </RouterLink>
            </van-col>
            <van-col span="6">
                <RouterLink to="/">
                    <van-icon name="pending-payment" />
                    <span>待支付</span>
                </RouterLink>
            </van-col>
            <van-col span="6">
                <RouterLink to="/">
                    <van-icon name="tosend" />
                    <span>已完成</span>
                </RouterLink>
            </van-col>
            <van-col span="6">
                <RouterLink to="/">
                    <van-icon name="logistics" />
                    <span>已取消</span>
                </RouterLink>
            </van-col>
        </van-row>
        <!-- 底部导航 -->
        <TripFooter />
    </div>

</template>

<style scoped>
/* 页面布局样式 */
.page-mine {
  padding: 16px;
  background-color: #f5f5f5f5;
}

/* 标题栏样式 */
.van-nav-bar {
  background-color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

/* 用户信息样式 */
.user-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  padding: 16px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.avatar img {
  width: 64px;
   height: 64px;
   border-radius: 50%;
   margin-right: 16px;
}


.user-header div p {
  font-size: 18px;
   color: #33333333;
   margin:0px;
}

.btn-link {
  color: #ff4d4f;
  text-decoration: none;
  margin-left: auto;
}

.btn-link:hover {
  text-decoration: underline;
}

/* 订单菜单列表样式 */
.van-row {
  margin-bottom: 16px;
}

.van-col {
  text-align: center;
}

.van-icon {
  font-size: 24px;
  margin-bottom: 4px;
  /* color: #333333333; */
}

.van-icon + span {
  display: block;
  font-size: 14px;
  color: #666666;
}

/* 底部导航样式 */
.van-bottom-nav {
  background-color: #ffffff;
  box-shadow: 0 -1px 2px rgba(0, 0, 0, 0.1);
}

</style>