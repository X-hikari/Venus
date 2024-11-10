<template>
  <div>

    <!-- 标题部分 -->
    <h1>图文展示</h1>

    <!-- 导航说明 -->
    <nav class="navigation-bar">
      <ul>
        <li><router-link to="/result1/all">全部</router-link></li>
        <li><router-link to="/result1/explain">说明</router-link></li>
        <li><router-link to="/result1/activity">活动</router-link></li>
      </ul>
    </nav>

    <div>
      <router-view></router-view>
    </div>

  </div>

</template>

<script setup>
  import { ref } from 'vue'
  const name = 'result1'
</script>

<style>

.navigation-bar {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  /* text-align: center; */
}

.navigation-bar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.navigation-bar li {
  display: inline-block;
  margin-right: 10px;
}

.navigation-bar a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-bar a.router-link-active {
  color: #007bff;
}

</style>
