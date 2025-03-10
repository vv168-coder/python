<script setup>
//可以获取路由中携带的数据
import { RouterLink, RouterView,useRoute } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

const route = useRoute()//获得useRoute实例
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

    <div class="wrapper">
      <!-- <HelloWorld msg="我富有的很" /> -->

      <nav>
        <!-- <RouterLink to="/">首页home </RouterLink> -->
          <!-- RouterLink 类似于a标记可实现页面跳转，该标记支持路由地址匹配，to属性地址目标-->
        <!-- <RouterLink > -->
          <!-- 关于
          {{ route.params.id }}
          {{ route.query.sort }}
          {{ route.query.name }}
          {{ route.params.type }} -->


        <!-- </RouterLink> -->
      </nav>
    </div>
  </header>
<!-- 通过该标记显示路由地址所指向的组件内容 -->
  <RouterView />
</template>

<!-- <style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style> -->
