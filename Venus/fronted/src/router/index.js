// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // 假设首页内容在 home.vue 中
import result1 from '../views/result1.vue';

const routes = [
  { path: '/', redirect: '/home' }, // 自动重定向到 /home
  { path: '/home', name: 'Home', component: Home },
  { path: '/result1', name: 'result1', component: result1 },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
