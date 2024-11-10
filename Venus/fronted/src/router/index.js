// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // 假设首页内容在 home.vue 中
import result1 from '../views/Home/result1.vue';
import result2 from '../views/Home/result2.vue';
import result3 from '../views/Home/result3.vue';
import result4 from '../views/Home/result4.vue';
import about from '../views/about.vue';
import result1_all from '../views/Home/result1/result1_all.vue';
import explain from '../views/Home/result1/result1_explain.vue';
import activity from '../views/Home/result1/result1_activity.vue';

const routes = [
  { path: '/', redirect: '/home' }, // 自动重定向到 /home
  { path: '/home', name: 'Home', component: Home },
  { path: '/about', name: 'about', component: about },
  {
    path: '/result1',
    name: 'result1',
    component: result1,
    redirect: '/result1/all', // 默认重定向到 /result1/all
    children: [
      { path: 'all', name: 'result1_all', component: result1_all }, // 子路由定义为相对路径
      { path: 'explain', name: 'explain', component: explain }, 
      { path: 'activity', name: 'activity', component: activity }, 
    ],
  },
  
  {
    path: '/result2',
    name: 'result2',
    component: result2,
    children: [
    ],
  },

  {
    path: '/result3',
    name: 'result3',
    component: result3,
    children: [
    ],
  },

  {
    path: '/result4',
    name: 'result4',
    component: result4,
    children: [
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
