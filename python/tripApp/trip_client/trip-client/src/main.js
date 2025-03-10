import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'//导入路由工具
//引入vantui组件库
import Vant from 'vant';
// 引入vantui组件库样式
import 'vant/lib/index.css'


const app = createApp(App)


app.use(router)//挂在路由工具
app.use(Vant)
app.mount('#app')
