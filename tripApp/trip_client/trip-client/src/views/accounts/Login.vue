<script setup>
import Copyright from '@/components/common/Copyright.vue';
import { ref } from 'vue';
import { useRouter,useRoute } from 'vue-router';
import { ajax } from '@/utils/ajax'
import { AccountsApis } from '@/utils/apis';
import { showToast } from 'vant'

// 针对路由操作
const router = useRouter();
const route = useRoute();

// 用户名的验证规则
const rulename=ref([{
    required: true,//用户名组件中通过该属性开启验证
    message: '请输入用户名',//验证失败的提示信息
},{
    pattern: /1\d{10}/,//用户名组件中通过该属性开启必填验证,
    message: '请输入正确的手机号',//验证失败的提示信息
}])

const goBack = () => {
    router.go(-1);
}

const form = ref({
    username: '',
    password: '',
})

const onSubmit = async () => {
    // 1. 验证输入
    if (!form.value.username || !form.value.password) {
        showToast('请输入用户名和密码');
        return;  // 如果没有输入用户名或密码，直接返回
    }

    try {
        // 2. 调用登录接口
        const response = await ajax.post(AccountsApis.loginUrl, {
            username: form.value.username,
            password: form.value.password,
        });

        const { data } = response;

        if (data.success) {
            // 3. 登录成功后的处理
            showToast('登录成功');
            router.push({ name: 'Mine' });  // 跳转到个人中心页面
        } else {
            // 4. 登录失败的处理（根据返回的数据，提示错误信息）
            showToast(data.message || '登录失败，请检查用户名或密码');
        }

    } catch (error) {
        // 5. 网络或其他错误的处理
        showToast('网络错误，请稍后再试');
        console.error('登录请求失败', error);  // 打印错误信息以便调试
    }
};




</script>

<template>
    <div class="page-account-login">
         <!--导航条  -->
         <van-nav-bar title="用户登录" left-text="返回" left-arrow @click-left="goBack"></van-nav-bar>
         <!-- 表单输入 -->
        <van-form @submit="onSubmit">
            <!-- 文本框 -->
            <van-field v-model="form.username" label="用户名" placeholder="请输入用户名" maxlength="11" :rules="rulename"></van-field>
            <!-- 密码框 -->
            <van-field v-model="form.password" type="password" label="密码" placeholder="请输入密码" 
            :rules="[{required: true}]"></van-field>
            <div style="margin:16px">
                <van-button round block native-type="submit" type="info">登录</van-button>
            </div>
        </van-form>
        <!-- 文字提示 -->
         <div>
            登录表示同意<a href="#">用户使用协议</a><a href="#">隐私条款</a>
         </div>
         <div>
            没有账户？<RouterLink :to="{name:'AccountRegister'}">点击注册</RouterLink>
         </div>
         <!-- 版权信息 -->
          <Copyright></Copyright>
    </div>
</template>


<style scoped>
/* 页面布局样式 */
.page-account-login {
  padding: 16px;
  background-color: #f5f5f5f5;
}

/* 导航条样式 */
.van-nav-bar {
  background-color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

/* 表单样式 */
.van-form {
  margin-top: 16px;
  background-color: #ffffff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 文本框样式 */
.van-field {
  margin-bottom: 16px;
}

/* 按钮样式 */
.van-button {
  width: 100%;
  padding: 12px;
  background-color: #4CAF50;
  color: #ffffff;
  border-radius: 4px;
  font-size: 16px;
}

.van-button:hover {
  background-color: #45a145;
}

/* 文字提示样式 */
div a {
  color: #ff4d4f;
  text-decoration: none;
  margin-right: 8px;
}

div a:hover {
  text-decoration: underline;
}

/* 版权信息样式 */
.Copyright {
  margin-top: 16px;
  text-align: center;
  color: #999;
  font-size: 12px;
}
</style>