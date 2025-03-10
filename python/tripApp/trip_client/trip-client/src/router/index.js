import { createRouter, createWebHistory } from 'vue-router'//导入配置路由的工具
import HomeView from '../views/HomeView.vue'//导入组件
import Search  from '../views/Search.vue'
import SightComment from '@/views/sight/SightComment.vue'
import SightDetail from '@/views/sight/SightDetail.vue'
import SightList from '@/views/sight/SightList.vue'
import SightImg from '@/views/sight/SightImg.vue'
import SightInfo from '@/views/sight/SightInfo.vue'
import SightAddComment from '@/views/sight/SightAddComment.vue'
import AccountLogin from '@/views/accounts/Login.vue'
import AccountRegister from '@/views/accounts/Register.vue'
import Mine from '@/components/Mine.vue'
//创建路由对象
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),//路由模式
  routes: [//配置路由地址
    {//{}路由的目标
      path: '/',//目标地址
      name: 'home',//路由名称
      component: HomeView//路由目标
    },
    {//{}路由的目标
      path: '/search',//目标地址
      name: 'Search',//路由名称
      component: Search//路由目标
    },
    {//{}路由的目标
      path: '/mine',//目标地址
      name: 'Mine',//路由名称
      component: Mine//路由目标
    },    
    {//{}路由的目标
      path: '/sight/comment/:id',//目标地址
      name: 'SightComment',//路由名称
      component: SightComment//路由目标
    },
    {//{}路由的目标
      path: '/sight/sight/detail/:id',//目标地址
      name: 'SightDetail',//路由名称
      component: SightDetail//路由目标
    },
    {//{}路由的目标
      path: '/sight/info/:id',//目标地址
      name: 'SightInfo',//路由名称
      component: SightInfo//路由目标
    },
    {//{}路由的目标
      path: '/sight/image/:id',//目标地址
      name: 'SightImg',//路由名称
      component: SightImg//路由目标
    },
    {//{}路由的目标
      path: '/sight/list',//目标地址
      name: 'SightList',//路由名称
      component: SightList//路由目标
    },
    {//{}路由的目标
      path: '/sight/sight/addcomment/:id',//目标地址
      name: 'SightAddComment',//路由名称
      component: SightAddComment//路由目标
    },
    {//{}路由的目标
      path: '/account/login',//目标地址
      name: 'AccountLogin',//路由名称
      component: AccountLogin//路由目标
    }, 
    {//{}路由的目标
      path: '/account/register',//目标地址
      name: 'AccountRegister',//路由名称
      component: AccountRegister//路由目标
    },  

  ]
})

//暴露路由对象
export default router
